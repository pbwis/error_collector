from django.urls import path
from .views import upload_file_view, list_of_data


app_name = 'csvs'

urlpatterns = [
    path('', upload_file_view, name='upload-view'),
    path('list', list_of_data, name='list' ),
]