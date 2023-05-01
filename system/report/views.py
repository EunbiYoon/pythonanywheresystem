from django.shortcuts import render,redirect, get_object_or_404
from .models import Category, Post, Comment
from .forms import CommentForm
import datetime

def homeView(request):
    posts = Post.objects.all()
    context={
        'posts_set':posts
    }
    return render(request, 'home.html', context)

def detailView(request, slug, pk):
    post = Post.objects.get(slug=slug, pk=pk)
    new_comment=None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=post)
        if comment_form.is_valid():
            name = request.user.username
            body = comment_form.cleaned_data['comment_body']
            new_comment = Comment(post=post, commenter_name=name, comment_body=body)
            new_comment.save()
        else:
            print('form is invalid')    
    else:
        comment_form = CommentForm()    


    context = {
        'post_detail':post,
        'new_comment': new_comment,
        'form_detail':comment_form,
    }

    return render(request, 'detail.html', context)

def categoryView(request, slug):
    category=Category.objects.get(slug=slug)
    context={
        'category_pair':category
    }
    return render(request,'category.html', context)



