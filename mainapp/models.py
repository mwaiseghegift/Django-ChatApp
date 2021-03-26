from django.db import models

# Create your models here.

class Chat(models.Model):
    room_no = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    
    def __str__(self):
        return f"{self.room_no} - {self.message}"
    
