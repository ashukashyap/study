from django.shortcuts import render
from blog.models import Post
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def bloghome(request):
    allPost = Post.objects.all()
    context = {'allPost':allPost,}

    return render(request,'blog/bloghome.html' ,context)



@login_required
def blogpost(request,slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post':post}
    return render(request,'blog/blogpost.html' ,context)




