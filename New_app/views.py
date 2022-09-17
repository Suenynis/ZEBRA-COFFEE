from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from New_app.forms import RegisterForm
from New_app.models import User
from django.http import HttpResponseRedirect

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
            User.objects.create(**user_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'New_app/registration.html', context={'user_form': user_form})

class UserEditFormView(View):
    def get(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = RegisterForm(instance=user)
        return render(request, 'New_app/edit.html',context={'user_form': user_form, 'profile_id': profile_id})

    def post(self, request, profile_id):
        user = User.objects.get(id=profile_id)
        user_form = RegisterForm(request.POST, instance=user)

        if user_form.is_valid():
            user_form.save()
        return render(request, 'New_app/edit.html', context={'user_form': user_form, 'profile_id': profile_id})