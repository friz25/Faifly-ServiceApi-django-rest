from django.db import models # дописали [6]
from rest_framework import generics, permissions, viewsets # [14]
# from rest_framework.response import Response # удалили [9]
# from rest_framework.views import APIView # удалили [9]
from django_filters.rest_framework import DjangoFilterBackend

from .models import Service, Appointment, Review, Rating, TimeLocation, Worker, Location, Schedule


from .serializers import (
    ServiceListSerializer,
    ServiceDetailSerializer,

    ReviewSerializer,
    ReviewCreateSerializer,
    CreateRatingSerializer,

    AppointmentListSerializer,
    AppointmentDetailSerializer,

    FilterReviewListSerializer,
    RecursiveSerializer,

    WorkerListSelializer,
    WorkerDetailSelializer,
    LocationListSelializer,
    LocationDetailSelializer,
    ScheduleListSelializer,
    ScheduleDetailSelializer,
)
from .service import get_client_ip, ServiceFilter, PaginationService, AppointmentFilter, PaginationAppointment

"""###########################################################################
*ReadOnlyModelViewSet - может выводить и список и одну запись
###########################################################################"""

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    """ [GET] Вывод списка Услуг \n
    * ReadOnlyModelViewSet - может выводить и список и одну запись """
    filter_backends = (DjangoFilterBackend,) #подключили фильт django
    filterset_class = ServiceFilter # http://127.0.0.1:8001/api/v1/service/?cost_min=100&cost_max=2000
    pagination_class = PaginationService

    # def get_queryset(self):
    #     services = Service.objects.filter(draft=False).annotate(
    #         rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
    #     ).annotate(
    #         middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
    #     )
    #     return services

    def get_queryset(self):
        services = Service.objects.filter(draft=False)
        return services

    def get_serializer_class(self):
        if self.action == 'list':
            return ServiceListSerializer
        elif self.action == 'retrieve':
            return ServiceDetailSerializer

class AppointmentViewSet(viewsets.ReadOnlyModelViewSet):
    """ [GET] Вывод списка Записей на приём \n
    * ReadOnlyModelViewSet - может выводить и список и одну запись """
    filter_backends = (DjangoFilterBackend,) #подключили фильт django
    filterset_class = AppointmentFilter # http://127.0.0.1:8001/api/v1/appointment/?dutation_min=10&dutation_max=60
    pagination_class = PaginationAppointment

    # def get_queryset(self):
    #     appointments = Appointment.objects.filter(draft=False).annotate(
    #         rating_user=models.Count("ratings", filter=models.Q(ratings__ip=get_client_ip(self.request)))
    #     ).annotate(
    #         middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
    #     )
    #     return appointments

    def get_queryset(self):
        appointments = Appointment.objects.filter(draft=False)
        return appointments

    def get_serializer_class(self):
        if self.action == 'list':
            return AppointmentListSerializer
        elif self.action == 'retrieve':
            return AppointmentDetailSerializer

"""###########################################################################
*ModelViewSet - позволяет нам реализ-ть сразу добавление, вывод списка, одной записи, обновления, удаления записи
###########################################################################"""

class ReviewCreateViewSet(viewsets.ModelViewSet):
    """ [POST] Добавление комментария (к специалисту) [14]"""
    serializer_class = ReviewCreateSerializer

class AddStarRatingViewSet(viewsets.ModelViewSet):
    """[POST] Добавление рейтинга специалисту """
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        """ возвращает IP пользователя """
        serializer.save(ip=get_client_ip(self.request))
"""################################ Rating ######################################
"""

class WorkersViewSet(viewsets.ReadOnlyModelViewSet):
    """" Вывод списка Специалистов [8] """
    queryset = Worker.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return WorkerListSelializer
        elif self.action == 'retrieve':
            return WorkerDetailSelializer

class LocationsViewSet(viewsets.ReadOnlyModelViewSet):
    """" Вывод списка Локаций / Кабинетов [8] """
    queryset = Location.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return LocationListSelializer
        elif self.action == 'retrieve':
            return LocationDetailSelializer

class SchedulesViewSet(viewsets.ReadOnlyModelViewSet):
    """" Вывод списка Смен специалистов [8] """
    queryset = Schedule.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ScheduleListSelializer
        elif self.action == 'retrieve':
            return ScheduleDetailSelializer