from django.views.generic import TemplateView, CreateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import StudentSignUpForm
from .models import User
from django.views.generic import UpdateView
from .forms import UserProfileForm
from django.shortcuts import render, redirect
import os
import ssl
import smtplib
from django.core.mail.backends.smtp import EmailBackend

from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView, 
    PasswordResetCompleteView
)
from django.urls import reverse_lazy
from .forms import CustomPasswordResetForm # Твоя форма со стилями auth-input

class MainPageView(TemplateView):
    template_name = 'index.html'

class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'profile.html'
    success_url = reverse_lazy('profile') # Лучше использовать reverse_lazy по имени пути
    login_url = '/login/'

    def get_object(self, queryset=None):
        # Это гарантирует, что юзер редактирует СВОЙ профиль, а не чужой по ID
        return self.request.user


class SignUpView(CreateView):
    form_class = StudentSignUpForm  
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class MyLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'auth-input'})
        return form


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class AboutClubView(ListView):
    model = User
    template_name = 'about.html'
    context_object_name = 'players'
    paginate_by = 4
    
    def get_queryset(self):
        # Теперь здесь только те, кому ты лично дал "метку" в админке
        return User.objects.filter(is_in_roster=True).order_by('-rating')


class ScheduleView(TemplateView):
    template_name = 'schedule.html'

class KnowledgeView(TemplateView):
    template_name = 'knowledge.html'

class JoinClubView(TemplateView):
    template_name = 'join.html'

class UserPasswordResetView(PasswordResetView):
    # Указываем новый уникальный путь
    template_name = 'main/auth/password_reset_form.html' 
    form_class = CustomPasswordResetForm
    success_url = reverse_lazy('password_reset_done')
    # Не забудь про шаблон письма, его тоже переложи в новую папку
    email_template_name = 'main/auth/password_reset_email.html'
    

class UserPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'main/auth/password_reset_done.html'

# Во views.py добавь метод в UserPasswordResetConfirmView
class UserPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'main/auth/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            field.widget.attrs.update({'class': 'auth-input'})
        return form



# --------------------------------------------------------- e-mail
class UserPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'main/auth/password_reset_complete.html'

def unlock_site(request):
    if request.method == 'POST':
        # Берем пароль из .env. Если там пусто, по умолчанию будет '1234'
        correct_password = os.getenv('SITE_PASSWORD')
        
        if request.POST.get('site_password') == correct_password:
            request.session['site_unlocked'] = True
            return redirect('home')  # Проверь, что в urls.py главная называется 'home'
            
    return render(request, 'unlock.html')