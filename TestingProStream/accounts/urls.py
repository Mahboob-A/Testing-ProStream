

from django.urls import path

from .views import RegisterAPI, RegisterAPI2

urlpatterns = [
        path('save/',  RegisterAPI.as_view(), name='save_data'), 
        path('save2/',  RegisterAPI2.as_view(), name='save_data_2'), 
]
