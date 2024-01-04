import random

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm

from users.models import User


class RegisterView(CreateView):
    """ Контроллер регистрации пользователя """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:verification')

    def form_valid(self, form):
        """ Форма отправки кода подтверждения почты пользователя """
        list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if form.is_valid():
            email_verification = ''
            for i in range(8):
                rand_idx = random.randint(0, len(list)-1)
                email_verification += str(rand_idx)

            form.email_verification = email_verification
            user = form.save()
            user.email_verification = email_verification
            send_mail(
                subject='Поздравляем с регистрацией!',
                message=f'Подтвердите вашу регистрацию, введите код подтверждения {user.email_verification}',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user.email]
            )
            return super().form_valid(form)


class VerificationView(TemplateView):
    """ Контроллер верификации почты пользователя """
    template_name = 'users/verification_email.html'
    success_url = reverse_lazy('users:login')

    def post(self, request):
        email_verification = request.POST.get('email_verification')
        user_code = User.objects.filter(email_verification=email_verification).first()

        if user_code.email_verification == email_verification:
            user_code.is_active = True
            user_code.save()
            return redirect('users:login')
        else:
            return redirect('users:verification_error')


class ErrorVerification(TemplateView):
    """ Контроллер ошибочно введенного кода верификации"""
    template_name = 'users/verification_email_error.html'
    success_url = reverse_lazy('users:verification')


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """ Контроллер профиля пользователя """
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    """ Контроллер генерации автоматически созданного пароля """
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_mail(
        subject='Вы сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('catalog:main_page'))
