"""
СЕРИАЛИЗАТОРЫ - нужны чтоб приобразовывать типы данных python > в json (и наоборот)
"""
from rest_framework import serializers

from .models import Service, Appointment, Review, Rating, TimeLocation, Worker, Location, Schedule


class ServiceListSerializer(serializers.ModelSerializer):
    """Список услуг """

    # rating_user = serializers.BooleanField()
    # middle_star = serializers.IntegerField()

    class Meta:
        model = Service
        # fields = ("id", "title", "tagline", "service_category", "rating_user", "middle_star")
        fields = ("id", "title", "tagline", "service_category")


class AppointmentListSerializer(serializers.ModelSerializer):
    """Список Записей на услугу """

    # rating_user = serializers.BooleanField()
    # middle_star = serializers.IntegerField()

    class Meta:
        model = Appointment
        # fields = ("id", "title", "tagline", "service_category", "rating_user", "middle_star")
        fields = ("id", "user_name", "service")


class FilterReviewListSerializer(serializers.ListSerializer):
    """Фильтр комментов, только parents """

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод рекурсивно children """

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


"""################################ ACTOR ######################################
"""


class WorkerListSelializer(serializers.ModelSerializer):
    """ Вывод списка специалистов """

    class Meta:
        model = Worker
        fields = ("id", "name", "image")


class WorkerDetailSelializer(serializers.ModelSerializer):
    """ Вывод полного описания специалистов """

    class Meta:
        model = Worker
        fields = "__all__"


class LocationListSelializer(serializers.ModelSerializer):
    """ Вывод списка Локаций / Кабинетов """

    class Meta:
        model = Location
        fields = ("id", "name", "image")


class LocationDetailSelializer(serializers.ModelSerializer):
    """ Вывод полного описания Локаций / Кабинетов """

    class Meta:
        model = Location
        fields = "__all__"


class ScheduleListSelializer(serializers.ModelSerializer):
    """ Вывод списка Рабочих смен специалистов """

    class Meta:
        model = Schedule
        fields = ("id", "name")


class ScheduleDetailSelializer(serializers.ModelSerializer):
    """ Вывод полного описания Рабочих смен специалистов """

    class Meta:
        model = Schedule
        fields = "__all__"


"""################################ ACTOR ######################################
"""


class ReviewCreateSerializer(serializers.ModelSerializer):
    """[POST] Добавление комментария (к специалисту) """

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """[GET] Вывод комментария (к специалисту) """
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilterReviewListSerializer
        model = Review
        fields = ("name", "text", "children")


"""################################ COMMENT ######################################
"""


class ServiceDetailSerializer(serializers.ModelSerializer):
    """ Полный список Услуг """
    service_category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    workers = WorkerListSelializer(read_only=True, many=True)

    # reviews = ReviewSerializer(many=True)

    class Meta:
        model = Service
        exclude = ("draft",)


class AppointmentDetailSerializer(serializers.ModelSerializer):
    """ Полный список Записей на приём """
    service_category = serializers.SlugRelatedField(slug_field="name", read_only=True)
    service = ServiceListSerializer(read_only=True, many=True)
    schedule = ScheduleListSelializer(read_only=True, many=True)

    # reviews = ReviewSerializer(many=True)

    class Meta:
        model = Appointment
        exclude = ("draft",)


"""################################ Service - Appointment ######################################
"""


class CreateRatingSerializer(serializers.ModelSerializer):
    """ Добавление рейтинга (специалисту) пользователем"""

    class Meta:
        model = Rating
        fields = ("star", "worker")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            worker=validated_data.get('worker', None),
            defaults={"star": validated_data.get('star')}
        )
        return rating
