from django.db import models
from django.conf import settings

class Ats(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    address = models.CharField(max_length=100, blank=True, default='')

class Olt(models.Model):
    ip = models.GenericIPAddressField()
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    model = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    ats = models.ForeignKey(Ats,related_name='olts', on_delete=models.CASCADE)

class Ont(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    serial = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    template = models.CharField(max_length=50)
    profile = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    olt = models.ForeignKey(Olt,related_name='onts',on_delete=models.CASCADE,blank=True,null=True)

class Rssi(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rx = models.FloatField(blank=True,null=True)
    tx = models.FloatField(blank=True,null=True)
    ont = models.ForeignKey(Ont,related_name='rssi',on_delete=models.CASCADE)

class Operation(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    type_operation = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100)
    reason = models.CharField(max_length=200)
    ont = models.ForeignKey(Ont, related_name='operation',on_delete=models.CASCADE,null=True, blank=True)