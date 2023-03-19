from django.db import models


class Wallet(models.Model):
    name = models.CharField(max_length=100)
    budget = models.FloatField()
    incomes = models.ManyToManyField("finance.Incomes", blank=True)
    expanses = models.ManyToManyField("finance.Expenses", blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


class Incomes(models.Model):
    name = models.CharField(max_length=100)
    incomes = models.FloatField()
    type = models.ForeignKey("finance.TypeIncomes", on_delete=models.PROTECT)
    typeFreqIncomes = models.ForeignKey("finance.TypeFreq", on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)


class Expenses(models.Model):
    name = models.CharField(max_length=100)
    expenses = models.FloatField()
    type = models.ForeignKey("finance.TypeExpenses", on_delete=models.PROTECT)
    typeFreqExpenses = models.ForeignKey("finance.TypeFreq", on_delete=models.PROTECT)
    timestamp = models.DateTimeField(auto_now_add=True)


class TypeIncomes(models.Model):
    name = models.CharField(max_length=50)


class TypeExpenses(models.Model):
    name = models.CharField(max_length=50)


class TypeFreq(models.Model):
    name = models.CharField(max_length=50)
    days = models.IntegerField()
