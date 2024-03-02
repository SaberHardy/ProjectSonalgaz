from django.shortcuts import render, redirect, get_object_or_404

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
from appSongaz.models import File


def index(request):
    return render(request, 'pages/index.html')


def dashboard(request):
    return render(request, 'pages/dashboard.html')


#
def editprofile(request):
    return render(request, 'pages/editprofile.html')


def documents(request):
    all_files = File.objects.all()
    context = {
        'all_files': all_files
    }
    return render(request, 'pages/documents.html', context)


def document(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('documents')
    else:
        form = FileForm()
    return render(request, 'pages/document.html', {
        'form': form
    })


def delete_file(request, id):
    file_instance = get_object_or_404(File, id=id)
    file_instance.delete()
    return redirect('documents')

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
