from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to='images')
    slug = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("blogs:blog_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title
    

    
