from django.db import models


# Shared Model
class SharedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


# Create your models here.
class Todo(SharedModel):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
