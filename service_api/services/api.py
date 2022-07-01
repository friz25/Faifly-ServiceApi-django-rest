"""
ViewSet - позволяет описывать методы, и к этим методам описывать http запросы с клиентской стороны
"""
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

# from .models import Actor
from .models import Worker, Location, Schedule

from .serializers import (
    # ActorListSelializer,
    # ActorDetailSelializer,
    WorkerListSelializer,
    WorkerDetailSelializer,
    LocationListSelializer,
    LocationDetailSelializer,
    ScheduleListSelializer,
    ScheduleDetailSelializer,
)
'''
class ActorViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Actor.objeects.all()
        serializer = ActorListSelializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Actor.objects.all()
        actor = get_object_or_404(queryset, pk=pk)
        serializer = ActorDetailSelializer(actor)
        return Response(serializer.data)
'''
class WorkerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Worker.objects.all()
        serializer = WorkerListSelializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Worker.objects.all()
        actor = get_object_or_404(queryset, pk=pk)
        serializer = WorkerDetailSelializer(actor)
        return Response(serializer.data)

class LocationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationListSelializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Location.objects.all()
        actor = get_object_or_404(queryset, pk=pk)
        serializer = LocationDetailSelializer(actor)
        return Response(serializer.data)

class ScheduleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Schedule.objects.all()
        serializer = ScheduleListSelializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Schedule.objects.all()
        actor = get_object_or_404(queryset, pk=pk)
        serializer = ScheduleDetailSelializer(actor)
        return Response(serializer.data)