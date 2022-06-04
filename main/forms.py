from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import User
from .models import Product, Rating


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form__input input', 'placeholder': 'Введите логин'}
    ))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form__input input', 'placeholder': 'Введите пароль'}
    ))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Имя пользователя', widget=forms.TextInput(
        attrs={'class': 'form__input input', 'placeholder': 'Введите логин', 'autocomplete': 'off'}
    ))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form__input input', 'placeholder': 'Введите пароль', 'autocomplete': 'off'}
    ))
    password2 = forms.CharField(label='Пароль повторно', widget=forms.PasswordInput(
        attrs={'class': 'form__input input', 'placeholder': 'Введите пароль повторно', 'autocomplete': 'off'}
    ))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['order_to', 'product_type', 'product_number', 'product_mark', 'product_much', 'text']
        widgets = {
            'order_to': forms.Select(attrs={'class': 'form__input input'}),
            'product_type': forms.Select(attrs={'class': 'form__input input'}),
            'product_number': forms.Select(attrs={'class': 'form__input input'}),
            'product_mark': forms.Select(attrs={'class': 'form__input input'}),
            'product_much': forms.TextInput(attrs={'class': 'form__input input'}),
            'text': forms.Textarea(attrs={'class': 'form__textarea input', 'placeholder': 'Примечания'}),
        }


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['title', 'mark']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form__input input'}),
            'mark': forms.TextInput(attrs={'class': 'form__input input', 'placeholder': 'Примечания', 'type': 'number', 'min': '0', 'max': '5'}),
        }
