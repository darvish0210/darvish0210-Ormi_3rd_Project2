from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)  
    views = models.PositiveIntegerField(default=0)
    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
    def __str__(self):
        return self.title

