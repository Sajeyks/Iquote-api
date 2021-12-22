from django.db.models import fields
from rest_framework import serializers
from .models import *


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['author', 'content']