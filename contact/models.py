from django.db import models

# Create your models here.


class Message(models.Model):
    TYPE_CHOICES = (
        ('query', 'Query/Question'),
        ('testimonial', 'Testimonial'),
    )
    name = models.CharField(max_length=254)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField(max_length=1000)
    contact_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default='query')
    is_approved = models.BooleanField(default=False)
    rating = models.PositiveIntegerField(choices=[(i, i) for i in range(6)], default=5) # Rating from 0 to 5

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=50, default="Subject")
    content = models.TextField()
    rating = models.PositiveIntegerField(default=0, choices=[(i, i) for i in range(6)]) # Rating from 0 to 5
    created_at = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name