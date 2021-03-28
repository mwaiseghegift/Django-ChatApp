from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()
class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='message_user', null=True, blank=True)
    room_no = models.CharField(max_length=255)
    message = models.TextField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.room_no} - {self.message}"
    
