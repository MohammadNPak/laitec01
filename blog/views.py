from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Post, Comment, UserProfile
# Create your views here.


def index(request):
    return render(request, 'blog/index.html', context={})


def post(request, pk, slug):

    if request.method == "GET":
        try:
            post = (Post.objects
                    .select_related('author')
                    .select_related('author__user')
                    .prefetch_related ('like')
                    .prefetch_related ('dislike')
                    .prefetch_related ('comment_set')
                    .prefetch_related ('comment_set__author')
                    .prefetch_related ('comment_set__author__user')
                    .prefetch_related ('comment_set__like')
                    .prefetch_related ('comment_set__dislike')
                    .get(pk=pk)
                    )
            post = get_object_or_404(Post, pk=pk)
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
