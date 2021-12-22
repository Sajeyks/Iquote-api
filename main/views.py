from django.shortcuts import render
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from .models import *
from rest_framework.response import Response
from .serializer import *
import random

# Create your views here.
def pick_random_object():
    return random.randrange(1, Quote.objects.all().count() + 1)


class QuotesView(APIView):
    serializer_class = QuoteSerializer

    def get(self, request):
        for detail in Quote.objects.all().filter(id = pick_random_object()):
            detail = {"author": detail.author, "content": detail.content}
        return Response(detail)
