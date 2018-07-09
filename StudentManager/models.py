from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Student(models.Model):
    roll_no = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    college_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

