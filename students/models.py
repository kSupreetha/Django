from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_no = models.CharField(max_length=20)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.roll_no})"
