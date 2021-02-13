from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    email = models.CharField(max_length=122)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name + " - "+self.email
