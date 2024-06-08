from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# registerUser function will be called when /accounts/registerUser/ path is accessed, which is defined in accounts/urls.py
def registerUser(request):
    return render(request, 'accounts/registerUser.html')
