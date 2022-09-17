from django.shortcuts import render
from django.views import View


# Create your views here.

def apper(request):
    return render(request, 'New_app/index.html', {})
