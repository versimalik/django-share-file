from django.shortcuts import render, HttpResponseRedirect
from .models import File
from django.urls import reverse

# Create your views here.

def index(request):
    all_files = File.objects.order_by('-created_at')

    context = {
        'files' : all_files
    }

    return render(request, 'main/index.html', context)

def create(request):
    file = request.FILES['file']
    description = request.POST['description']
    new_file = File.objects.create(file=file, description=description)

    new_file.filename = str(new_file.file).split("/")[1]
    new_file.filetype = new_file.filename.split(".")[1]
    new_file.save()

    # print(type(str(new_file.file)))

    return HttpResponseRedirect(reverse('index'))