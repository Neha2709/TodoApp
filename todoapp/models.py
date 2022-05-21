from django.db import models

# Create your models here.

STATUS_CHOICES = (
    ('Not Started','Not Started'),
    ('In progress', 'In progress'),
    ('Completed','Completed'),
)

class TodoItem(models.Model):
    content = models.CharField(max_length=400)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default='Not Started')
    ETA = models.DateField()
