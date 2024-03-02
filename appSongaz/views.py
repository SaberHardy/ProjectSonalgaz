import mimetypes
import os
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from appSongaz.forms import FileForm
from appSongaz.models import File


def index(request):
    return render(request, 'pages/index.html')


def dashboard(request):
    count_all_files = File.objects.all().count()
    all_users = User.objects.all()
    context = {
        'count_all_files': count_all_files,
        'all_users': all_users
    }
    return render(request, 'pages/dashboard.html', context)


#
def editprofile(request):
    return render(request, 'pages/editprofile.html')





def documents(request):
    all_files = File.objects.all()
    context = {
        'all_files': all_files,
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


def download_file(request, pk):
    file_instance = get_object_or_404(File, pk=pk)
    file_path = os.path.join(settings.MEDIA_ROOT, str(file_instance.file))

    with open(file_path, 'rb') as file:
        response = HttpResponse(file.read())

    content_type, encoding = mimetypes.guess_type(file_instance.file.name)
    response['Content-Type'] = content_type
    response['Content-Disposition'] = f'attachment; filename="{file_instance.file.name}"'

    return response

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
