from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=250)
    view_count = models.IntegerField(default=0)
    views = models.CharField(max_length=250)
    tags = models.CharField(max_length=250)

    def __str__(self):
        return self.question    