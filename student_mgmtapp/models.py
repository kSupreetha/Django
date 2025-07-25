from django.db import models

class student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    roll_no = models.CharField(max_length=20)
    course = models.CharField(max_length=100)

    def _str_(self):
        return f"{self.name} ({self.roll_no})"
