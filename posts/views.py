from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm


def Index(request):
    # if methid is POST
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Yes, Save
            form.save()
            # Rdirect to Home
            return HttpResponseRedirect('/')

        else:
            # No, Show error
            return HttpResponseRedirect(form.errors.as_json())



    posts = Post.objects.all().order_by('-created_at') [:20]
    return render(request,'posts.html',
                {'posts': posts})

def delete(request, post_id):
    # find post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts = Post.objects.get(id = post_id)
    if request.method=="GET":
        return render(request, 'edit.html', {'posts':posts})


    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance = posts) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else :
            return HttpResponseRedirect(form.errors.as_json())
    return render(request, 'edit.html', {'post':posts})

def like(request, post_id):
    like = Post.objects.get(id = post_id)
    like.likes +=1 
    like.save()
    return HttpResponseRedirect('/')
    
    