from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User 
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.
'''

title
content
publish_date

author
image
tags
'''

class Post(models.Model):
    author = models.ForeignKey(User,related_name='post_author' , on_delete=models.SET_NULL,null=True)
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=30000)
    publish_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='posts')
    tags = TaggableManager()
    slug = models.SlugField(null=True,blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comment_author' , on_delete=models.SET_NULL,null=True)
    post = models.ForeignKey(Post,related_name='comment_post', on_delete=models.CASCADE)
    Comment = models.TextField(max_length=1000)
    create_at = models.DateTimeField(default=timezone.now)

    