import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserForm
from users.models import User


# Create your views here.


class LoginView(BaseLoginView):
    template_name = 'users/login.html'


class LogoutView(BaseLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:verifications_1')
    template_name = 'users/register.html'

    def form_valid(self, form):
        self.object = form.save()
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(10)])
        self.object.verification = new_password
        self.object.is_active = False
        self.object.save()
        send_mail(
            subject='Поздравляем с регистрацией',
            message=f'Для завершения регистрации пройдите по ссылке '
                    f'http://127.0.0.1:8000/users/verification/?new_password={new_password}!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email],
        )
        return super().form_valid(form)


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    success_url = reverse_lazy('users:profile')
    form_class = UserForm

    def get_object(self, queryset=None):
        return self.request.user

@login_required
def generate_new_password(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')
        for item in User.objects.all():
            if item.email == user_email:
                new_password = ''.join([str(random.randint(0, 9)) for _ in range(20)])
                item.set_password(new_password)
                item.save()
                send_mail(
                    subject='Ваш новый пароль',
                    message=f'Ваш новый пароль: {new_password}',
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user_email],
                )
    return render(request, 'users/genpassword.html')


def verification_user(request):
    user_password = request.GET['new_password']
    for item in User.objects.all():
        if item.verification == user_password:
            item.is_active = True
            item.save()
    return render(request, 'users/verification.html')


def verification_user_1(request):
    return render(request, 'users/verification_1.html')
