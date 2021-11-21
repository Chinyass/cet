from rest_framework import serializers
#from django.contrib.auth.models import User
from gpon.models import *

class AtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ats
        fields = '__all__'

class OltSerializer(serializers.ModelSerializer):
    onts = serializers.PrimaryKeyRelatedField(many=True, queryset=Ont.objects.all())
    class Meta:
        model = Olt
        fields = '__all__'

class OntSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ont
        fields = '__all__'
    

class RssiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rssi
        fields = '__all__'