from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from rest_framework import generics

from gpon.models import *
from gpon.serializers import *

class AtsList(APIView):
    def get(self, request, format=None):
        ats = Ats.objects.all()
        serializer = AtsSerializer(ats,many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = AtsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AtsDetail(APIView):
    def get_object(self, pk):
        try:
            return Ats.objects.get(pk=pk)
        except Ats.DoesNotExists:
            raise Http404
    
    def get(self, request, pk, format=None):
        ats = self.get_object(pk)
        serializer = AtsSerializer(ats)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        ats = self.get_object(pk)
        serializer = AtsSerializer(ats,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        ats = self.get_object(pk)
        ats.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class OltList(generics.ListCreateAPIView):
    queryset = Olt.objects.all()
    serializer_class = OltSerializer

class OltDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Olt.objects.all()
    serializer_class = OltSerializer

class OntList(generics.ListCreateAPIView):
    queryset = Ont.objects.all()
    serializer_class = OntSerializer

class OntDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ont.objects.all()
    serializer_class = OntSerializer

class RssiList(generics.ListCreateAPIView):
    queryset = Rssi.objects.all()
    serializer_class = RssiSerializer

class RssiDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rssi.objects.all()
    serializer_class = RssiSerializer