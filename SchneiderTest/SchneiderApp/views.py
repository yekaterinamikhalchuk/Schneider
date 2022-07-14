from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import FileUpload

# Создайте здесь представления.

def upload_file(request):
    if request.method == 'POST':
        form = FileUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:
        form = FileUpload
    return render(request, 'files/file_upload.html', {'form':form})
