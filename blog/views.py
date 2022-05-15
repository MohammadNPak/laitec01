from django.http import HttpResponse, Http404
from django.db.models import Count, Prefetch, F
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, UserProfile

# Create your views here.


def index(request):
    return render(request, 'blog/index.html', context={})

@login_required
def post(request, slug):
    try:
        if request.method == "POST":
            p = Comment(author=request.user.userprofile,
                        content_object=Post.objects.get(slug=slug),
                        body=request.POST['text'])
            p.save()
        post = (Post.objects.prefetch_related(
            Prefetch('comment',
                     queryset=(Comment.objects
                               .annotate(username=F('author__user__username'))
                               .select_related('author')
                               .annotate(like_count=Count('like'))
                               .annotate(dislike_count=Count('dislike'))
                               .annotate(comments_count=Count('comment'))
                               )
                     )
        )
            .annotate(like_count=Count('like'))
            .annotate(dislike_count=Count('dislike'))
            .annotate(comments_count=Count('comment'))
            .annotate(username=F('author__user__username'))
            .select_related('author')
            .get(slug=slug)
        )
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'blog/post.html', context={"post": post})


def posts(request):
    if request.method == "POST":
        new_post = Post(author=request.user.userprofile,
                        title=request.POST['title'],
                        body=request.POST['body'])
        new_post.save()
    p = (Post.objects.all()
             .select_related('author')
             .annotate(like_count=Count('like'))
             .annotate(dislike_count=Count('dislike'))
             .annotate(comments_count=Count('comment'))
             .annotate(username=F('author__user__username'))
             .order_by('-date'))
        # print(posts)
    return render(request, 'blog/posts.html', context={"posts": p})
