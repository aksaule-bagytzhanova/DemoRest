from django.urls import path
from django.urls.conf import include
from cars.views import CarsListView, CarCreateView, CarDetailView

app_name = 'car'
urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('all/', CarsListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),

    

]
