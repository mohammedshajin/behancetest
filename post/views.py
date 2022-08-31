from multiprocessing import context
from django.shortcuts import render
from . models import Post

def home(request):
    post = Post.objects.all()
    context = {'post':post}
    return render(request, 'index.html', context)
