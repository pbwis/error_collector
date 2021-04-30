from django.db import models

class Post(models.Model):
    display_name = models.CharField(null=True, max_length=100)
    display_version = models.CharField(null=True, max_length=100)
    publisher = models.CharField(null=True, max_length=100)
    install_date = models.CharField(null=True, max_length=100)


    def __str__(self):
        return self.display_name[:50]
    

class Csv(models.Model):
    file_name = models.FileField(upload_to='data')
    uploaded = models.DateTimeField(auto_now_add=True)
    activated = models.BooleanField(default=False)

    def __str__(self):
        return f"File id: {self.id}"
    