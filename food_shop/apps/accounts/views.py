from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .forms import EmailVerification, UserLoginForm, UserProfileForm, UserRegistrationForm
from .models import User

class UserLoginView(LoginView):
    form_class = UserLoginForm
    template_name = 'login.html'

class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    success_message = 'Congratulations! You are successfully registered!'

class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile.html'

    def get_success_url(self):
        return reverse_lazy('profile', args=(self.object.id,))

class EmailVerificationView(TemplateView):
    template_name = 'email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)

        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))

class Logout(SuccessMessageMixin, TemplateView):
    template_name = 'logout.html'
    success_message = 'Вы успешно вышли из аккаунта!'

    def get_success_url(self):
        return reverse_lazy('index')
