from django.db import models

class User(models.Model):
    user_id = models.CharField(primary_key = True, max_length=50)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.username
