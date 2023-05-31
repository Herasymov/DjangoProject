from django.contrib import admin
from .models import Country, Item, Cart


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)

    def __str__(self):
        return self.name


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

    def __str__(self):
        return self.name


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'country')
    filter_horizontal = ('items',)

    def __str__(self):
        return f"Cart {self.id}"
