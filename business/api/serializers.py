from rest_framework import serializers
from business.models import Value

class ValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Value
        fields = ['id', 'timestamp', 'value']