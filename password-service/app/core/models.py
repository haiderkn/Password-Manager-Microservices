from django.db import models


class LoginCredential(models.Model):
    """Model for Saving email,password for different website."""
    user_id = models.UUIDField(blank=True, null=True)
    link = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.link
