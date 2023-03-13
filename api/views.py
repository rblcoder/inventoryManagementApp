from rest_framework import viewsets
from rest_framework.response import Response
from products.models import Category, Currency, Location
from .serializers import CategorySerializer, CurrencySerializer, LocationSerializer


class CategoryViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)


class CurrencyViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Currency.objects.all()
        serializer = CurrencySerializer(queryset, many=True)
        return Response(serializer.data)


class LocationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)
