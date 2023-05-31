from rest_framework import serializers
from .models import Cart, Item, Country


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    country = CountrySerializer(allow_null=True)

    class Meta:
        model = Cart
        fields = ['id', 'items', 'country']
