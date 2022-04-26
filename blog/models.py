from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Post()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    posts = models.ForeignKey("Post", on_delete=models.CASCADE)
    comment = models.ForeignKey("Comment", on_delete=models.CASCADE)


class Comment(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, null=True, blank=True)


class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="like", null=True, blank=True)
    dislike = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="dislike", null=True, blank=True)

    def count_like(self):
        return 1
        # self.objects.select_related('like').annotate()
