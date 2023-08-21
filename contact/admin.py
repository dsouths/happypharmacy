from django.contrib import admin
from .models import Message, Testimonial

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'rating', 'created_at', 'is_approved') 
    list_editable = ('is_approved',) 

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'contact_type', 'is_approved')
