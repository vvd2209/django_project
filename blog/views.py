from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify
from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'body',)
    success_url = reverse_lazy('blog:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'body',)

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:list')


def toggle_activity(request, pk):
    """ Отображает смену статуса статьи блога 'активно'/'неактивно'"""
    blog_item = get_object_or_404(Blog, pk=pk)
    if blog_item.is_publish:
        blog_item.is_publish = False
    else:
        blog_item.is_publish = True

    blog_item.save()

    return redirect(reverse('blog:list'))


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        """ При открытии статьи увеличивает счетчик просмотров статьи блога """
        self.object = super().get_object(queryset)
        self.object.count_view += 1
        self.object.save()
        return self.object
