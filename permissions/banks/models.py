from django.db import models


class Bank(models.Model):
    label = models.CharField(max_length=30)
    # Analyst
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)


class BankAccount(models.Model):
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    # Customer
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    # Just example (You won't use int field for money)
    balance = models.IntegerField()
