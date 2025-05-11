from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'telegram_id', 'is_2fa_enabled', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'}),
            'role': forms.Select(attrs={'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'}),
            'telegram_id': forms.TextInput(attrs={'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'}),
            'is_2fa_enabled': forms.CheckboxInput(attrs={'class': 'w-5 h-5 border-red-300 rounded focus:ring-2 focus:ring-red-500'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Удаляем метку "Password" и "Password confirmation" для единообразия
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'
        self.fields['password1'].widget.attrs.update({'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'})
        self.fields['password2'].widget.attrs.update({'class': 'w-full border border-red-300 rounded-md px-4 py-3 focus:outline-none focus:ring-2 focus:ring-red-500 text-lg'})