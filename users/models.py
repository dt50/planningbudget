from django.db import models
from django.contrib.auth.models import User


class UserExp(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    wallet = models.ForeignKey("finance.Wallet", on_delete=models.CASCADE)
