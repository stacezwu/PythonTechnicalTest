from django.db.models.fields import DateField
from rest_framework import serializers
from .models import Bond

class BondSerializer(serializers.ModelSerializer):
    class Meta:
        # isin = serializers.CharField()
        # size = serializers.IntegerField()
        # currency = serializers.CharField()
        # maturity = serializers.DateField()
        # lei = serializers.CharField()
        model = Bond
        fields = ['isin', 'size', 'currency', 'maturity', 'lei', 'legal_name']
