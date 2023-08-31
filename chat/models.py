from django.db import models
from user.models import User


def save_chat_media(instance, filename):
    return 'chat_messages/user/%d/%s' % (instance.sender.id, filename)


class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    text_message = models.TextField(blank=True, null=True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="created_time")
    modified_time = models.DateTimeField(auto_now=True, verbose_name="modified_time")

    def __str__(self):
        return f'{self.sender} to {self.receiver}: {self.text_message}'
