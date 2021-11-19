from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from gpon.models import *
from gpon.serializers import *

@csrf_exempt
def ats_list(request):
    print('USER',type(request.user))
    if request.method == 'GET':
        ats = Ats.objects.all()
        serializer = AtsSerializer(ats,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AtsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def ats_detail(request,pk):
    print(pk)
    try:
        ats = Ats.objects.get(pk=pk)
    except Snipet.DoesNotExists:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = AtsSerializer(ats)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = AtsSerializer(ats,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        ats.delete()
        return HttpResponse(status=204)

@csrf_exempt
def olt_list(request):
    if request.method == 'GET':
        olt = Olt.objects.all()
        serializer = OltSerializer(olt,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = OltSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt
def olt_detail(request,pk):
    print(pk)
    try:
        olt = Olt.objects.get(pk=pk)
    except Snipet.DoesNotExists:
        return HttpResponse(status=404)
    
    if request.method == 'GET':
        serializer = OltSerializer(olt)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = OltSerializer(olt,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        
        return JsonResponse(serializer.errors,status=400)

    elif request.method == 'DELETE':
        olt.delete()
        return HttpResponse(status=204)