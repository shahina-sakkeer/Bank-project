from django.db import models

# Create your models here.

class Formfill(models.Model):
    name=models.CharField(max_length=200)
    dob=models.DateField()
    age=models.PositiveIntegerField()
    email=models.EmailField()
    phone_number=models.PositiveIntegerField()
    gender=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    district=models.CharField(max_length=200)
    branch=models.CharField(max_length=200)
    account_type=models.CharField(max_length=200)
    credit_card = models.BooleanField(default=False)
    debit_card = models.BooleanField(default=False)
    cheque_book = models.BooleanField(default=False)


    def __str__(self):
        return self.name

