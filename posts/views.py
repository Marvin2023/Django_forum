from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django.forms import forms


def index(request):
    #if the method is POST
    if request.method == 'POST':
        form = PostForm(request.POST)
    #If the form is valid
        if form.is_valid(): 
           #Yes , save
           form.save()
    #Redirect to Home
           return HttpResponseRedirect('/')
        else:
            #No, Show Error
             return HttpResponseRedirect(form.errors.as_json())
    #Get all posts,limit = 20
    posts= Post.objects.all().order_by('-created_at')[:20]

    
    return render(request, 'posts.html',
    {'posts':posts})     #posts -  A QuerySet is a collection of data from a database. A QuerySet is built up as a list of objects. QuerySets makes it easier to get the data you actually need, by allowing you to filter and order the data.


def delete(request, post_id):
    post= Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')
