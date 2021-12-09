from django.db import models

# Create your models here.
class test(models.Model):
    test_name=models.CharField(max_length=100)
    description=models.CharField(max_length=100)
    rate=models.IntegerField()
    procedures=models.CharField(max_length=200)

    def __str__(self):
        return self.test_name

class bookings(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    phone=models.BigIntegerField()
    age=models.IntegerField()
    date=models.DateField()
    test=models.CharField(max_length=100)
    message=models.TextField()

    def __str__(self):
        return self.name