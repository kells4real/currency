from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .api import CurrencySerializer
from .models import Currency


class CurrencyApiList(APIView):

    def get(self, request):
        currencies = Currency.objects.all()
        serializer = CurrencySerializer(currencies, many=True)

        return Response(serializer.data)

    def post(self):
        pass


class CurrencyDetail(APIView):

    def get(self, request, slug):
        currencies = Currency.objects.get(slug=slug)
        serializer = CurrencySerializer(currencies)

        return Response(serializer.data)

    def post(self):
        pass
