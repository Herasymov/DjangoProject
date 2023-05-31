from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APIRequestFactory
from .models import Cart, Item, Country
from .serializers import CartSerializer, ItemSerializer, CountrySerializer
from .views import cart_create_or_update, cart_retrieve, check_cart, item_list, country_list

factory = APIRequestFactory()


class CartAPITest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.item = Item.objects.create(name='Item 1', price=10.0)
        self.country = Country.objects.create(name='Country 1')
        self.cart = Cart.objects.create(user=self.user)
        self.cart.items.add(self.item)
        self.cart.country = self.country
        self.cart.save()

        self.access_token = AccessToken.for_user(self.user)

    def test_cart_create_or_update(self):
        request = factory.post('/create/', {'items': [self.item.id], 'country': self.country.id})
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {str(self.access_token)}'
        response = cart_create_or_update(request)
        self.assertEqual(response.status_code, 200)
        cart = Cart.objects.get(user=self.user)
        self.assertEqual(cart.items.count(), 1)
        self.assertEqual(cart.country, self.country)

    def test_cart_retrieve(self):
        request = factory.get('/retrieve/')
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {str(self.access_token)}'
        response = cart_retrieve(request)
        self.assertEqual(response.status_code, 200)
        serializer = CartSerializer(self.cart)
        self.assertEqual(response.data, serializer.data)

    def test_check_cart(self):
        request = factory.get('/check_cart/')
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {str(self.access_token)}'
        response = check_cart(request)
        self.assertEqual(response.status_code, 200)
        serializer = CartSerializer(self.cart)
        self.assertEqual(response.data, serializer.data)

    def test_item_list(self):
        request = factory.get('/items/')
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {str(self.access_token)}'
        response = item_list(request)
        self.assertEqual(response.status_code, 200)
        queryset = Item.objects.all()
        serializer = ItemSerializer(queryset, many=True)
        self.assertEqual(response.data, serializer.data)

    def test_country_list(self):
        request = factory.get('/countries/')
        request.META['HTTP_AUTHORIZATION'] = f'Bearer {str(self.access_token)}'
        response = country_list(request)
        self.assertEqual(response.status_code, 200)
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        self.assertEqual(response.data, serializer.data)
