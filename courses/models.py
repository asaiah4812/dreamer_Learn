from django.db import models

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    access = models.CharField(max_length=16, choices=(
        ('Anyone', 'Anyone'),
        ('Email_required', 'Email_required'),
    ), default='Draft')
    status = models.CharField(max_length=10, choices=(
        ('Published', 'Published'),
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
    ), default='Draft')
