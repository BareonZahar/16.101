from django import forms
from django.core.exceptions import ValidationError

from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpform(UserCreationForm):
    username = forms.CharField(label='логин', help_text='Придумайте слово более 5 букв')
    password1 = forms.CharField(label='пароль', help_text='Пароль'
                                , widget=forms.PasswordInput(attrs={'autocomplete': "new-password"}))
    password2 = forms.CharField(label='подтверждение', help_text='Повторите пароль'
                                , widget=forms.PasswordInput(attrs={'autocomplete': "new-password"}))
    email = forms.EmailField(label='почта', widget=forms.TextInput(attrs={'placeholder': "qwe@gmail.ru"}))
    first_name = forms.CharField(label='имя', max_length=20)
    last_name = forms.CharField(label='фамилия', max_length=20, required=False)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        new = User.objects.filter(username=username)
        if new.count():
            raise ValidationError("Такой пользователь уже существует")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        new = User.objects.filter(email=email)
        if new.count():
            raise ValidationError("Электронная почта уже существует")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадает")
        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user






# class CommentForm(forms.ModelForm):
#     class Meta:
#         model = Comment
#         fields = ('name', 'email', 'body')

    # def __str__(self):
    #     return self.name,self.body

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     self.fields['address'].required = False




# class My_Form(forms.ModelForm):
#     class Meta:     форма для того чтоб указать какое поле не обязательное
#         model = My_Class
#         fields = ('first_name', 'last_name' , 'address')
#     def __init__(self, *args, **kwargs):
#         super(My_Form, self).__init__(*args, **kwargs)
#         self.fields['address'].required = False