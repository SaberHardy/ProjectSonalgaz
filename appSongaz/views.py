from django.shortcuts import render, redirect

# from django.contrib.auth import authenticate, login, logout
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_protect
# import os
# import time
# from django.conf import settings
# from .forms import FileForm
# from django.contrib.auth import logout
# from django.views.decorators.cache import never_cache
from django.core.files.storage import FileSystemStorage

from appSongaz.forms import FileForm


def index(request):
    return render(request, 'pages/index.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


#
def editprofile(request):
    return render(request, 'pages/editprofile.html')


def documents(request):
    return render(request, 'pages/document.html')


def document(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileForm()
    return render(request, 'pages/document.html', {
        'form': form
    })
#
#
# # Login Code 'index'
#
#
# def index(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None and user.is_active:
#             login(request, user)
#             return redirect('dashboard')
#         else:
#             error_message = "Invalid username or password"
#             return render(request, 'pages/index.html', {'error_message': error_message})
#
#     return render(request, 'pages/index.html')
#
#
# def document(request):
#     if request.method == 'POST':
#         form = FileForm(request.POST, request.FILES)
#         if form.is_valid():
#             file_instance = form.save(commit=False)
#             file_instance.uploader = request.user
#             file_instance.save()
#             form = FileForm()
#     else:
#         form = FileForm()
#     return render(request, 'pages/document.html', {'form': form})
#
#
# def upload_success(request):
#     return render(request, 'pages/upload_success.html')
#
#
# def logout_view(request):
#     logout(request)
#     return render(request, 'pages/logout.html')
