from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Post()
from django.urls import reverse
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username


class Comment(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.ManyToManyField(
        UserProfile, related_name="comment_likes", null=True, blank=True)
    dislike = models.ManyToManyField(
        UserProfile, related_name='comment_dislikes', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.post.slug})+f"#{self.pk}"
    
    def count_like(self):
        return self.like.count()

    def count_dislike(self):
        return self.dislike.count()

    def __str__(self) -> str:
        return f"{self.author.user.username}|{self.post.title[:20]}|{self.body[:20]}..."


class Post(models.Model):
    slug = models.SlugField(max_length=100,blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(
        UserProfile, related_name="post_likes", null=True, blank=True)
    dislike = models.ManyToManyField(
        UserProfile, related_name='post_dislikes', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f"{slugify(self.title)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def count_like(self):
        return self.like.count()

    def count_dislike(self):
        return self.dislike.count()

    def get_absolute_url(self):
        return reverse("post", kwargs={"pk":self.pk,"slug": self.slug})

    def __str__(self) -> str:
        return f"{self.author.user.username}|{self.title[:20]}|{self.body[:20]}..."
