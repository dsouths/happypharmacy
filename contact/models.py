from django.db import models

# Create your models here.


class Message(models.Model):
    """contact form model"""
    name = models.CharField(max_length=254)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name