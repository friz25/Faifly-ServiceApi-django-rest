"""
ViewSet - позволяет описывать методы, и к этим методам описывать http запросы с клиентской стороны
"""
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Worker, Location, Schedule

from .serializers import (
    WorkerListSelializer,
    WorkerDetailSelializer,
    LocationListSelializer,
    LocationDetailSelializer,
    ScheduleListSelializer,
    ScheduleDetailSelializer,
)


class WorkerViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Worker.objects.all()
        serializer = WorkerListSelializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Worker.objects.all()
        worker = get_object_or_404(queryset, pk=pk)
        serializer = WorkerDetailSelializer(worker)
        return Response(serializer.data)


class LocationViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationListSelializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Location.objects.all()
        location = get_object_or_404(queryset, pk=pk)
        serializer = LocationDetailSelializer(location)
        return Response(serializer.data)


class ScheduleViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Schedule.objects.all()
        serializer = ScheduleListSelializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Schedule.objects.all()
        schedule = get_object_or_404(queryset, pk=pk)
        serializer = ScheduleDetailSelializer(schedule)
        return Response(serializer.data)
