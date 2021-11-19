from django.urls import path
from . import views

urlpatterns = [
    path('ats/<int:pk>', views.ats_detail,name='ats_list'),
    path('ats', views.ats_list),
    path('olt/<int:pk>', views.olt_detail,name='olt_list'),
    path('olt', views.olt_list),

]