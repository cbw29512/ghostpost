from django.db import models
from django.utils import timezone
# Create your models here.

class PostItem(models.Model):
    post_title = models.CharField(max_length=50)
    body = models.CharField(max_length=280)
    date = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.post_title
""""
One model to represent both boasts and roasts
Boolean to tell whether it's a boast or a roast
CharField to put the content of the post in
IntegerField for up votes
IntegerField for down votes
DateTimeField for submission time
"""