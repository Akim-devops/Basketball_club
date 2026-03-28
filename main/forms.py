from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import get_user_model
from .models import User

User = get_user_model()

class StudentSignUpForm(UserCreationForm):
    # Если вы хотите, чтобы поле email было в начале и с валидацией:
    email = forms.EmailField(required=True, label="Электронная почта")

    class Meta:
        model = User
        # Указываем только те поля, которые юзер заполняет при регистрации
        # 'username' можно оставить, если он нужен в БД (Django его требует)
        fields = ("email", "username", "position") 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'auth-input',
                'placeholder': field.label
            })


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'auth-input',
                'placeholder': 'Введите ваш Email'
            })



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'height', 'weight', 'avatar']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Накидываем твои стили на инпуты
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'auth-input'})

