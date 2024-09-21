from django.db import models
import uuid

# Create your models here.

def handle_upload(instance, filename):
    return f"{filename}"

class Course(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to=handle_upload)
    access = models.CharField(max_length=16, choices=(
        ('Anyone', 'Anyone'),
        ('Email_required', 'Email_required'),
    ), default='Draft')
    status = models.CharField(max_length=10, choices=(
        ('Published', 'Published'),
        ('Draft', 'Draft'),
        ('Pending', 'Pending'),
    ), default='Draft')

    def __str__(self):
        return self.title
