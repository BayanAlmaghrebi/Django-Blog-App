from django.db import models

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
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=30000)
    publish_date = models.DateTimeField()