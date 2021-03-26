from django.urls import path
from .import views

app_name = 'blogs'

urlpatterns = [
     
    path("blog/",views.bloghome,name='bloghome'),
    path('blogs/<slug>/',views.blogpost,name='blogpost'),
   


]
