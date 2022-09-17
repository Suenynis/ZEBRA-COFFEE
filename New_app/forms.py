from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    email = forms.EmailField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100)