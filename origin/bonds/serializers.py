from django.contrib.auth.models import User
from django.db.models.fields import DateField
from rest_framework import serializers
from .models import Bond

class BondSerializer(serializers.ModelSerializer):
    userid = serializers.HiddenField(default = serializers.CurrentUserDefault())

    class Meta:
        model = Bond
        fields = ['userid','isin', 'size', 'currency', 'maturity', 'lei', 'legal_name']
