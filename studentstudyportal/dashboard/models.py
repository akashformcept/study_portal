from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

# Create your models here.

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()



# showing real names in database

    def __str__(Self):
        return Self.title

    class Meta():
        verbose_name = "notes"
        verbose_name_plural = "notes"


class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished  = models.BooleanField(default=False)

    def __str__(Self):
        return Self.title

    # class Meta():
    #     verbose_name = "notes"
    #     verbose_name_plural = "notes"
class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    is_finished  = models.BooleanField(default=False)

    def __str__(Self):
        return Self.title


