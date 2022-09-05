from django.urls import path 
from FeeStructure import views 

urlpatterns = [
    path('', views.dashboard, name="Dashboard"),
    path('insert-data', views.enter_data, name='DataEnter'), 
    path('retrieve-data', views.download_data, name="DataRetrieval"), 
]
