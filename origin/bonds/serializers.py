from django.contrib.auth.models import User
from django.db.models.fields import DateField
from rest_framework import serializers
from .models import Bond

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ()

class BondSerializer(serializers.ModelSerializer):
    userid = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        # isin = serializers.CharField()
        # size = serializers.IntegerField()
        # currency = serializers.CharField()
        # maturity = serializers.DateField()
        # lei = serializers.CharField()
        model = Bond
        fields = ['userid','isin', 'size', 'currency', 'maturity', 'lei', 'legal_name']
    # userid = serializers.HiddenField(default=None, write_only=True)
