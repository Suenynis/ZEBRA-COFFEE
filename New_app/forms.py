from django import forms
from New_app.models import User

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'