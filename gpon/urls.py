from django.urls import path
from . import views

urlpatterns = [
    path('ats/<int:pk>', views.AtsDetail.as_view()),
    path('ats', views.AtsList.as_view()),
    path('olt/<int:pk>', views.OltDetail.as_view()),
    path('olt', views.OltList.as_view()),
    path('ont/<int:pk>', views.OntDetail.as_view()),
    path('ont', views.OntList.as_view()),
    path('rssi/<int:pk>', views.RssiDetail.as_view()),
    path('rssi', views.RssiList.as_view()),
    path('find_personal',views.find_personal)
]