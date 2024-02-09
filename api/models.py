from django.db import models

# Create your models here.
class Classroom(models.Model):
    name = models.CharField(max_length=255)
    invite = models.BooleanField()
    room_name = models.CharField(max_length=255)

    def __str__(self):
        return f"Class:{self.name} RoomName:{self.room_name} invite:{self.invite}"

    class Meta:
        unique_together = ('name', 'room_name')

class Chatroom(models.Model):
    room_id = models.CharField(primary_key=True, max_length=255)

class Message(models.Model):
    room_id = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    content = models.TextField()
    attachment_url = models.URLField()
