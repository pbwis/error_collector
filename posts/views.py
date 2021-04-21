import pandas as pd
from io import StringIO
from django.shortcuts import render
from .models import Post, Csv
import csv, os
from django.http import HttpResponse
from .forms import CsvModelForm
#from django.views.generic import ListView



def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts_list.html', {'posts': posts})


def read_csv(request):
    current_path = os.path.dirname(__file__)
    data_folder = os.path.join(current_path, data)
    os.path.join(data_folder, software.csv)
    file = file_path.open(mode="r", encoding="utf-8", newline=" ")
    pass


def upload_file(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            print(row)
    return render(request, 'posts/posts_list.html', {'form': form})