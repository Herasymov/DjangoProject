from django.urls import path

from .views import cart_create_or_update, cart_retrieve, item_list, check_cart, country_list

urlpatterns = [
    path('create/', cart_create_or_update, name='cart-create-or-update'),
    path('retrieve/', cart_retrieve, name='cart-retrieve'),
    path('check_cart/', check_cart, name='check_cart'),
    path('items/', item_list, name='items_list'),
    path('countries/', country_list, name='country_list'),
]
