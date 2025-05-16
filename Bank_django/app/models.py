from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=32)
    phone = models.IntegerField()
    gender = models.CharField(max_length=7)
    dob = models.DateField()
    aadhar = models.PositiveBigIntegerField(unique=True)
    address = models.TextField()
    account_type = models.CharField(max_length=32)
    account_number = models.BigAutoField(primary_key=True)
    pin = models.IntegerField(default=0)
    amount = models.IntegerField(default=5000)


