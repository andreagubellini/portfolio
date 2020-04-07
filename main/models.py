from django.db import models
from django.utils import timezone
# Create your models here.

from django.db import models

class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE,)
    title = models.CharField(max_length = 100)
    body = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(auto_now_add=True,
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

