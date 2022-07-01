from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter # [14]
from rest_framework.urlpatterns import format_suffix_patterns # [14]

from . import views

app_name = 'services'
urlpatterns = format_suffix_patterns([
    path("service/", views.ServiceViewSet.as_view({'get': 'list'})),
    # http://127.0.0.1:8000/api/v1/service/
    path("service/<int:pk>/", views.ServiceViewSet.as_view({'get': 'retrieve'})),
    # http://127.0.0.1:8000/api/v1/service/1
    path("appointment/", views.AppointmentViewSet.as_view({'get': 'list'})),
    # http://127.0.0.1:8000/api/v1/appointment/
    path("appointment/<int:pk>/", views.AppointmentViewSet.as_view({'get': 'retrieve'})),
    # http://127.0.0.1:8000/api/v1/appointment/1

    path("review/", views.ReviewCreateViewSet.as_view({'post': 'create'})),
    # http://127.0.0.1:8000/api/v1/review/
    path("rating/", views.AddStarRatingViewSet.as_view({'post': 'create'})),
    # http://127.0.0.1:8000/api/v1/rating/ {"star":3, "worker": 1}

    path("worker/", views.WorkersViewSet.as_view({'get': 'list'})),
    # [14] http://127.0.0.1:8000/api/v1/worker/
    path("worker/<int:pk>", views.WorkersViewSet.as_view({'get': 'retrieve'})),
    # [14] http://127.0.0.1:8000/api/v1/worker/1
    path("location/", views.LocationsViewSet.as_view({'get': 'list'})),
    # [14] http://127.0.0.1:8000/api/v1/location/
    path("location/<int:pk>", views.LocationsViewSet.as_view({'get': 'retrieve'})),
    # [14] http://127.0.0.1:8000/api/v1/location/1
    path("schedule/", views.SchedulesViewSet.as_view({'get': 'list'})),
    # [14] http://127.0.0.1:8000/api/v1/schedule/
    path("schedule/<int:pk>", views.SchedulesViewSet.as_view({'get': 'retrieve'})),
    # [14] http://127.0.0.1:8000/api/v1/schedule/1
])

""" [TESTS]
http://127.0.0.1:8000/api/v1/service/        #GOOD
http://127.0.0.1:8000/api/v1/service/1           #GOOD
http://127.0.0.1:8000/api/v1/appointment/       #GOOD
http://127.0.0.1:8000/api/v1/appointment/1      # ERROR 

http://127.0.0.1:8000/api/v1/review/                          #GOOD
http://127.0.0.1:8000/api/v1/rating/ {"star":3, "worker": 1}   #GOOD

http://127.0.0.1:8000/api/v1/worker/            #GOOD
http://127.0.0.1:8000/api/v1/worker/1          #GOOD
http://127.0.0.1:8000/api/v1/location/        #GOOD
http://127.0.0.1:8000/api/v1/location/1      #GOOD
http://127.0.0.1:8000/api/v1/schedule/         #GOOD
http://127.0.0.1:8000/api/v1/schedule/1         #GOOD

http://127.0.0.1:8000/auth/    #GOOD
http://127.0.0.1:8000/swagger/  #GOOD
"""
