from django_filters import rest_framework as filters # дописали [10]
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

# from .models import Movie # дописали [10]
from .models import Service, Appointment

"""################################ Pagination ######################################
"""
class PaginationService(PageNumberPagination):
    """ Пагинация [17] """
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
    """ Пагинация [17] """
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
    """ [10] """
    # genres = CharFilterInFilter(field_name='genres__name', lookup_expr='in')
    # year = filters.RangeFilter()
    #
    # class Meta:
    #     model = Service
    #     fields = ['genres', 'year']
    pass

class AppointmentFilter(filters.FilterSet):
    """ [10] """
    # genres = CharFilterInFilter(field_name='genres__name', lookup_expr='in')
    # year = filters.RangeFilter()
    #
    # class Meta:
    #     model = Appointment
    #     fields = ['genres', 'year']
    pass
"""################################ Filter ######################################
"""