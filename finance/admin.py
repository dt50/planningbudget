from django.contrib import admin
from .models import Wallet, Incomes, Expenses


@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    pass


@admin.register(Incomes)
class IncomesAdmin(admin.ModelAdmin):
    pass


@admin.register(Expenses)
class ExpansesAdmin(admin.ModelAdmin):
    pass
