from django_filters import rest_framework as filters  # дописали [10]
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Service, Appointment

"""################################ Pagination ######################################
"""


class PaginationService(PageNumberPagination):
    """ Пагинация Услуг (API) """
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        """ то каким образом мы будем выводить инфу о пагинации"""
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


class PaginationAppointment(PageNumberPagination):
    """ Пагинация Записей на приём (API) """
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        """ то каким образом мы будем выводить инфу о пагинации"""
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })


"""################################ Pagination ######################################
"""


def get_client_ip(request):
    """ Получение IP пользователя """
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """ [10] """
    pass


"""################################ Filter ######################################
"""


class ServiceFilter(filters.FilterSet):
    """ Фильтр Услуг (по Категориям услуг, Цене) [10] """
    # service_category = CharFilterInFilter(field_name='service_category__name', lookup_expr='in')
    # cost = filters.RangeFilter()
    #
    # class Meta:
    #     model = Service
    #     fields = ['service_category', 'cost']
    pass


class AppointmentFilter(filters.FilterSet):
    """ Фильтр Записей на приём (по Услугам, Категориям услуг) [10] """
    # service = CharFilterInFilter(field_name='service__title', lookup_expr='in')
    # service_category = CharFilterInFilter(field_name='service_category__name', lookup_expr='in')
    #
    # class Meta:
    #     model = Appointment
    #     fields = ['service', 'service_category']
    pass


"""################################ Filter ######################################
"""
