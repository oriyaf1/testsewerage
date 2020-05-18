from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Controller(models.Model):
    controller_x = models.FloatField(default=31.7760081)
    controller_y = models.FloatField(default=35.2353219)
    GREEN = 1
    YELLOW = 2
    ORANGE = 3
    RED = 4
    STATUS = [
        (GREEN, '1 - GREEN'),
        (YELLOW, '2 - YELLOW'),
        (ORANGE, '3 - ORANGE'),
        (RED, '4 - RED')
    ]
    status = models.IntegerField(choices=STATUS)
    installed_date = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "ID " + str(self.pk)

    
    def get_absolute_url(self):
        return reverse('controller-detail', kwargs={'pk': self.pk})