from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static 
from django.conf import settings
from posts import views as post_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', include('posts.urls')),
    #path('', post_views.posts_list, name='home'),
    path('', include('csvs.urls', namespace='csvs') )
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)