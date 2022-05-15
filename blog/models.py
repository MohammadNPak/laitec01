from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
# Create your models here.

# class Post()
from django.urls import reverse,reverse_lazy
from django.template.defaultfilters import slugify


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    bio = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.user.username
    
    def get_absolute_url(self):
        return reverse_lazy("profile", kwargs={"username": self.user.username})
    


class Comment(models.Model):
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # post = models.ForeignKey(
    #     "Post", on_delete=models.CASCADE)
    comment = GenericRelation("Comment")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    like = models.ManyToManyField(
        UserProfile, related_name="comment_likes")
    dislike = models.ManyToManyField(
        UserProfile, related_name='comment_dislikes')

    def get_absolute_url(self):
        return reverse("post", kwargs={"post_slug": self.post.slug})+f"#{self.pk}"
    
    # def __str__(self) -> str:
    #     return f"{self.author.user.username}|{self.post.title[:20]}|{self.body[:20]}..."


class Post(models.Model):
    slug = models.SlugField(max_length=100,blank=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(
        UserProfile, related_name="post_likes")
    dislike = models.ManyToManyField(
        UserProfile, related_name='post_dislikes')
    comment = GenericRelation(Comment)
    def save(self, *args, **kwargs):
        if not self.slug:
            slug = f"{self.id}-{slugify(self.title)}"
            self.slug = slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post", kwargs={"slug": self.slug})

    # def __str__(self) -> str:
    #     return f"{self.author.user.username}|{self.title[:20]}|{self.body[:20]}..."
