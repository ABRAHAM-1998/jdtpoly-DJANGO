# compEng/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class FacultyUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.username

class StudentMark(models.Model):
    name = models.CharField(max_length=255)
    roll = models.CharField(max_length=10)
    mark1 = models.IntegerField()
    mark2 = models.IntegerField()
    mark3 = models.IntegerField()

    @property
    def total_mark(self):
        return self.mark1 + self.mark2 + self.mark3

    @property
    def pass_fail_status(self):
        total = self.total_mark
        return 'Pass' if total >= 150 else 'Fail'