from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def home(request):
  posts = Post.objects,all()
  return render(request, 'employees/home.html', {'posts': posts})

def manager(request):
  posts = Post.objects,all()
  return render(request, 'employees/manager.html', {'posts': posts})

def intern(request):
  posts = Post.objects,all()
  return render(request, 'employees/intern.html', {'posts': posts})



