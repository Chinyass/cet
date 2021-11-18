from rest_framework import serializers
from gpon.models import *

class AtsSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    address = serializers.CharField(required=False, allow_blank=True, max_length=100)
    author = serializers.CharField()

    