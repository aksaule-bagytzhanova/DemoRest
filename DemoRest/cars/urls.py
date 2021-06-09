from django.urls import path
from django.urls.conf import include
from cars.views import *

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    

]
