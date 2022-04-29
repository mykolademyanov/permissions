from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    ANALYST = 1
    CUSTOMER = 2
    ROLE_CHOICES = (
      (ANALYST, 'analyst'),
      (CUSTOMER, 'customer'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return str(self.id)


class User(AbstractUser):
    roles = models.ManyToManyField(Role)

    @property
    def is_analyst(self):
        return self.roles.filter(id=Role.ANALYST).exists()

    @property
    def is_customer(self):
        return self.roles.filter(id=Role.ANALYST).exists()
