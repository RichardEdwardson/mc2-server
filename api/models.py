from django.db import models


# class Asset(models.Model):
#     label = models.CharField(max_length=255)
#     file = models.FileField(upload_to='classroom_asset')
    

#     def __str__(self):
#         return f"{self.label}: {self.file}"


class Classroom(models.Model):
    TERM_CHOICES = {
        'F': 'Fall',
        'S': 'Summer',
        'W': 'Winter',
    }
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    term = models.CharField(choices=TERM_CHOICES, max_length=255)
    # asset = models.ManyToManyField(Asset)
    # asset = models.ForeignKey(Asset, null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return f"{self.year} {self.term} {self.name}"

class Asset(models.Model):
    LABEL_CHOICES = {
        'img': 'Image Library',
        'csv': 'Formula Sheet',
    }
    label = models.CharField(max_length=255, choices=LABEL_CHOICES)
    file = models.FileField(upload_to='classroom_asset')
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return f"{self.label}"


class Chatroom(models.Model):
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)
    room_id = models.CharField(primary_key=True, max_length=255)


class Message(models.Model):
    room_id = models.ForeignKey(Chatroom, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    attachment_url = models.URLField(null=True)


class Attachment(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    file = models.FileField(upload_to='message_attachment')
