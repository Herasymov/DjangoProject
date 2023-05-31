from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, Item, Country
from .serializers import CartSerializer, ItemSerializer, CountrySerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def cart_create_or_update(request):
    user = request.user
    data = request.data

    cart, created = Cart.objects.get_or_create(user=user)

    cart.items.clear()
    item_ids = data.get('items', [])
    for item_id in item_ids:
        try:
            item = Item.objects.get(id=item_id)
            cart.items.add(item)
        except Item.DoesNotExist:
            pass

    cart.country_id = data.get('country', cart.country_id)

    cart.save()

    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_retrieve(request):
    user = request.user

    try:
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def check_cart(request):
    user = request.user

    try:
        cart = Cart.objects.get(user=user)
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    except Cart.DoesNotExist:
        return Response({'message': 'No cart found for the current user.'}, status=404)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def item_list(request):
    queryset = Item.objects.all()
    serializer = ItemSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def country_list(request):
    queryset = Country.objects.all()
    serializer = CountrySerializer(queryset, many=True)
    return Response(serializer.data)
