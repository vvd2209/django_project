from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from catalog.forms import ProductForm, VersionForm, ProductFormModerator
from catalog.models import Category, Contacts, Product, Version
from catalog.services import get_categories_cache


@login_required
def contacts(request):
    context = {
        'object_list': Contacts.objects.all(),
        'title': 'Наши контакты'
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')
    return render(request, 'catalog/contacts.html', context)


class MainPageListView(ListView):
    """ Контроллер главной страницы """
    model = Product
    template_name = 'catalog/main_page.html'
    extra_context = {
        'title': 'Bakery Market',
        'object_list': get_categories_cache
    }


class CategoryListView(ListView):
    """ Контроллер вывода всех категорий """
    model = Category
    extra_context = {
        'title': 'Наши вкусняши'
    }


class ProductListView(LoginRequiredMixin, ListView):
    """ Контроллер вывода продуктов только авторизованным пользователям (LoginRequiredMixin) """
    model = Product

    def get_queryset(self):
        """
        Возвращает выборку товаров по номеру категории
        """
        queryset = super().get_queryset().filter(
            category_id=self.kwargs.get('pk'),
        )

        if not self.request.user.is_staff:
            queryset = queryset.filter(owner=self.request.user)

        return queryset

    def get_context_data(self, *args, **kwargs):
        """
        Возвращает товары определенной категории,
        """
        context_data = super().get_context_data(*args, **kwargs)
        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Наши вкусняши {category_item.name}'

        return context_data


class ProductDetailView(DetailView):
    """ Контроллер просмотра продукта """
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = str(context['object'])
        context['version'] = Version.objects.filter(product=self.kwargs['pk'], is_active=True).order_by('-pk')
        return context


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """ Контроллер добавления продукта """
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'

    def get_success_url(self):
        return reverse('catalog:products', args=[self.object.category_id])

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """ Контроллер редактирования продукта """
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:categories')

    def get_form_class(self):
        if self.request.user.groups.filter(name='Модератор').exists():
            return ProductFormModerator
        else:
            return ProductForm

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class ProductDeleteView(DeleteView):
    """ Контроллер удаления продукта """
    model = Product
    success_url = reverse_lazy('catalog:categories')
