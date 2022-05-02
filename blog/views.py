from django.http import HttpResponse, Http404
from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, UserProfile

# Create your views here.


def index(request):
    return render(request, 'blog/index.html', context={})


def post(request, slug):

    if request.method == "GET":
        try:
            post = (Post.objects.filter(slug=slug)
                    .select_related('author')
                    .select_related('author__user')
                    .prefetch_related ('like')
                    .prefetch_related ('dislike')
                    .prefetch_related ('comment')
                    .prefetch_related ('comment__author')
                    .prefetch_related ('comment__author__user')
                    .prefetch_related ('comment__like')
                    .prefetch_related ('comment__dislike')
                    .annotate(  like_count=Count('like'),
                                dislike_count=Count('dislike'),
                                comments_count=Count('comment'))
                    .first()
                    )
        except Post.DoesNotExist:
            raise Http404("Post does not exist")

        return render(request, 'blog/post.html', context={"post": post})
    elif request.method == "POST":
        pass


def posts(request):
    if request.method == "GET":
        posts1 = Post.objects.all()
        # print(posts)
        return render(request, 'blog/posts.html', context={"posts": posts1})
    elif request.method == "POST":
        pass
