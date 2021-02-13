from django.db import models

# Create your models here.


class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.CharField(max_length=3000)
    author = models.CharField(max_length=200)
    slug = models.CharField(max_length=340)
    timestamp = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.title+" by "+self.author
