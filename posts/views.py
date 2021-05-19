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



def upload_file(request):
    form = CsvModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvModelForm()
        obj = Csv.objects.get(activated=False)
        with open(obj.file_name.path, 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    pass
                else:
                    row = "".join(row)
                    row = row.replace(";", " ")
                    row = row.split()
                    Post = row[1].upper()
                    print(row)
                    print(type(row))
            obj.activated = True
            obj.save()
    return render(request, 'posts/posts_list.html', {'form': form})


with file.path.open(mode="w", encoding='utf-8', newline="") as file:
    writer = csv.writer(file)
    for temp_list in posts:
        writer.writerow(temp_list)