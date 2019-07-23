from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=48)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    std_class = models.ForeignKey(Class, related_name="students", on_delete=models.CASCADE)

    def __str(slef):
        return self.name