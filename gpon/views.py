from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework import generics,authentication
from django.contrib.auth.models import User
from gpon.models import *
from gpon.serializers import *
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist
from .Snmp import Snmp

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@api_view(['POST'])
def find_ont(request):
    received_json_data = request.data
    ips = received_json_data['ips']
    serial = received_json_data['serial']
    for ip in ips:
        author = User.objects.get(pk=1)
        olt = Olt.objects.get(ip=ip)
        device = Snmp(ip,'private_otu')
        data = device.get_inform_ont(serial)
        if data['STATUS']:
            ont = Ont(  
                            author = author,
                            olt = olt,
                            pid = data['ID'],
                            port = data['PORT'],
                            serial = data['SERIAL'],
                            version = data['VERSION'],
                            model = data['MODEL'],
                            template = data['TEMPLATE'],
                            profile = data['PROFILE'],
                            personal = data['PERSONAL'],
                            login = data['LOGIN'],
                            password = data['PASSWORD'],
                            voip_enable = data['VOIP_ENABLE'],
                            voip_number = data['VOIP_NUMBER'],
                            voip_password = data['VOIP_PASSWORD']
                        )
            serializer = OntSerializer(ont)
            return Response({'status':True, 'data':serializer.data},status.HTTP_200_OK)

    return Response({'status':False,'data':False},status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def find_personal(request):
    received_json_data = request.data
    ips = received_json_data['ips']
    personal = received_json_data['personal']
    info = []
    for ip in ips:
        device = Snmp(ip,'private_otu')
        data = device.get_inform_acs_user(personal)
        if data:
            author = User.objects.get(pk=1)
            olt = Olt.objects.get(ip=ip)
            try:
                ont = Ont.objects.get(serial=data['SERIAL'])
                ont.author = author
                ont.olt = olt
                ont.pid = data['ID']
                ont.port = data['PORT']
                ont.version = data['VERSION']
                ont.model = data['MODEL']
                ont.template = data['TEMPLATE']
                ont.profile = data['PROFILE']
                ont.personal = data['PERSONAL']
                ont.login = data['LOGIN']
                ont.password = data['PASSWORD']
                ont.voip_enable = data['VOIP_ENABLE']
                ont.voip_number = data['VOIP_NUMBER']
                ont.voip_password = data['VOIP_PASSWORD']
                ont.save()

            except ObjectDoesNotExist:
                ont = Ont(  
                            author = author,
                            olt = olt,
                            pid = data['ID'],
                            port = data['PORT'],
                            serial = data['SERIAL'],
                            version = data['VERSION'],
                            model = data['MODEL'],
                            template = data['TEMPLATE'],
                            profile = data['PROFILE'],
                            personal = data['PERSONAL'],
                            login = data['LOGIN'],
                            password = data['PASSWORD'],
                            voip_enable = data['VOIP_ENABLE'],
                            voip_number = data['VOIP_NUMBER'],
                            voip_password = data['VOIP_PASSWORD']
                        )
                ont.save()

            operation = OperationFindPersonal(author=author, personal=personal,status=True,ont=ont)
            operation.save()
            serializer = OntSerializer(ont)
            info.append({'ip':ip,'status':True,'data':serializer.data})
            return Response({'status':True, 'data':info},status.HTTP_200_OK)
        else:
            info.append({'ip':ip,'status':False,'data':False})

    author = User.objects.get(pk=1)
    operation = OperationFindPersonal(author=author, personal=personal,status=False)
    operation.save()
    return Response({'status':False,'data':info},status.HTTP_500_INTERNAL_SERVER_ERROR)


class AtsList(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        #print(get_client_ip(request))
        #auth_header = authentication.get_authorization_header(request).split()
        #print(auth_header)
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