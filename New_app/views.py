from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from New_app.forms import RegisterForm
from New_app.models import User

# Create your views here.
class Home(TemplateView):
    template_name = 'New_app/index.html'

def apper(request):
    return render(request, 'New_app/index.html')

class Userform(View):
    def get(self, request):
        user_form = RegisterForm()
        return render(request, 'New_app/registration.html', {'user_form': user_form})
    def post(self, request):
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return render(request, 'New_app/registration.html', {'user_form': user_form})
        return render(request, 'New_app/registration.html', {'user_form': user_form})