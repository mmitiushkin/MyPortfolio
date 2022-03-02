from django.urls import path
from .views import works, work_details

urlpatterns = [
    path('', works, name='works'),
    path('details', work_details, name='work_details'),
]