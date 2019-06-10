from django.db import models
from .category import Category


class NotificationType(Category):
    pass


class Notification(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    recipiant = models.EmailField()
    notification_type = models.ForeignKey(NotificationType, models.SET_NULL,
                                          blank=True, null=True)

    def __str__(self):
        return self.name
