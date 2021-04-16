import pandas as pd
from io import StringIO
from django.shortcuts import render
from .models import Post
import csv, os
from django.http import HttpResponse
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


def read_csv2(request):

    passcsvfile = request.FILES['csv_file']
    data = pd.read_csv("software.csv")
    #You can create your custom dataframe here before converting it to html in next line
    data_html = data.to_html() 
    context = {'loaded_data': data_html}
    return render(request, "posts/posts_list.html", context)

    
def read_csv3(request):
    df = pd.read_csv('software.csv')

    return render(request, "posts/posts_list.html", {'df': df})
