from django.db import models
from datetime import date

from django.urls import reverse


class ServiceCategory(models.Model):
    """ Категории Услуги """
    name = models.CharField("Категория Услуги", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория Услуги"
        verbose_name_plural = "Категории Услуг"


class Worker(models.Model):
    """ Специалисты """
    name = models.CharField("Имя", max_length=100)
    speciality = models.CharField("Cпециализация", max_length=100)  # добавил
    email = models.EmailField("Email", max_length=100, default=None, blank=True)  # добавил
    phone = models.CharField("Телефон", max_length=14, default=None, blank=True)  # добавил
    social = models.CharField("Соц сеть/Мессенджер", max_length=100, default=None, blank=True)  # добавил
    social2 = models.CharField("Соц сеть/Мессенджер (2)", max_length=100, default=None, blank=True)  # добавил
    social3 = models.CharField("Соц сеть/Мессенджер (3)", max_length=100, default=None, blank=True)  # добавил
    age = models.PositiveSmallIntegerField("Возраст", default=0, blank=True)
    description = models.TextField("Описание", default=None, blank=True)
    image = models.ImageField("Изображение", upload_to="workers/", default=None, blank=True)
    draft = models.BooleanField("Черновик", default=False)  # добавил

    def __str__(self):
        return f'{self.name} ({self.speciality})'

    def get_review(self):  # добавил
        return self.reviews_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse('services:worker_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Специалисты"
        verbose_name_plural = "Специалисты"


class Location(models.Model):
    """ Локация / Кабинет """
    name = models.CharField("Кабинет", max_length=100)
    floor = models.PositiveIntegerField("Этаж", default=None, blank=True)
    adress = models.CharField("Адресс", max_length=100, default=None, blank=True)
    speciality = models.CharField("Cпециализация", max_length=100, default=None, blank=True)  # добавил
    description = models.TextField("Описание", default=None, blank=True)
    image = models.ImageField("Изображение", upload_to="locations/", default=None, blank=True)
    working_hours_start = models.TimeField("Открыто с", default="09:00", blank=True,
                                           help_text="указать время в формате '09:00'")
    working_hours_end = models.TimeField("Открыто до", default="18:00", blank=True,
                                         help_text="указать время в формате '18:00'")

    def __str__(self):
        return f'{self.adress} Кабинет {self.name}'

    def get_absolute_url(self):
        return reverse('services:location_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Локация / Кабинет"
        verbose_name_plural = "Локации / Кабинеты"


class Time(models.Model):
    """ Время (30минутный отрезок) """
    TIME_BEAT = [
        ('08:00:00', '08:00:00'), ('08:30:00', '08:30:00'),
        ('09:00:00', '09:00:00'), ('09:30:00', '09:30:00'),
        ('10:00', '10:00'), ('10:30', '10:30'),
        ('11:00', '11:00'), ('11:30', '11:30'),
        ('12:00', '12:00'), ('12:30', '12:30'),
        ('13:00', '13:00'), ('13:30', '13:30'),
        ('14:00', '14:00'), ('14:30', '14:30'),
        ('15:00', '15:00'), ('15:30', '15:30'),
        ('16:00', '16:00'), ('16:30', '16:30'),
        ('17:00', '17:00'), ('17:30', '17:30'),
        ('18:00', '18:00'), ('18:30', '18:30'),
        ('19:00', '19:00'), ('19:30', '19:30'),
        ('20:00', '20:00'), ('20:30', '20:30'),
        ('21:00', '21:00'), ('21:30', '21:30'),
    ]
    time_start = models.TimeField("Начало", default='09:00', help_text="указать время в формате '09:00'")
    time_end = models.TimeField("Конец", default='09:30', help_text="указать время в формате '09:30'")

    def __str__(self):
        return f'{self.time_start} - {self.time_end}'

    class Meta:
        verbose_name = "Время (30минутный отрезок)"
        verbose_name_plural = "Время (30минутный отрезок)"
        # ordering = ["-value"]


class TimeLocation(models.Model):
    """ ВремяМесто """
    ip = models.CharField("IP адрес", max_length=15)
    DAYS = [
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Черверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    ]
    day_of_week = models.PositiveIntegerField(choices=DAYS, default=1)
    time = models.ForeignKey(Time, on_delete=models.CASCADE, verbose_name="время")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, verbose_name="место",
                                 related_name="timelocation_location")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="специалист",
                               related_name="timelocation_worker", default=None, blank=True)

    def __str__(self):
        if self.day_of_week == 1:
            return f"Пн ({self.time}) ({self.location}) {self.worker}"
        elif self.day_of_week == 2:
            return f"Вт ({self.time}) ({self.location}) {self.worker}"
        elif self.day_of_week == 3:
            return f"Ср ({self.time}) ({self.location}) {self.worker}"
        elif self.day_of_week == 4:
            return f"Чт ({self.time}) ({self.location}) {self.worker}"
        elif self.day_of_week == 5:
            return f"Пт ({self.time}) ({self.location}) {self.worker}"
        elif self.day_of_week == 6:
            return f"Сб ({self.time}) ({self.location}) {self.worker}"
        else:
            return f"Вс ({self.time}) ({self.location}) {self.worker}"

    class Meta:
        verbose_name = "ВремяМесто"
        verbose_name_plural = "ВремяМесто"


class Schedule(models.Model):
    """ Рабочие смены специалиста """
    name = models.CharField("Название смены", max_length=100)
    """
    DAYS = [
        (1, 'Понедельник'),
        (2, 'Вторник'),
        (3, 'Среда'),
        (4, 'Черверг'),
        (5, 'Пятница'),
        (6, 'Суббота'),
        (7, 'Воскресенье'),
    ]
    day_of_week = models.PositiveIntegerField(max_length=1, choices=DAYS, default=1)
    schedule_start = models.TimeField("Начало смены", default="10:00", help_text="указать время в формате '10:00'")
    schedule_end = models.TimeField("Конец смены", default="12:00", help_text="указать время в формате '12:00'")
    """
    description = models.TextField("Описание", default=None, blank=True)
    timelocation = models.ManyToManyField(TimeLocation, verbose_name="ВремяМесто", related_name="timelocation",
                                          default=None)  # добавил
    draft = models.BooleanField("Черновик", default=False)  # добавил

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('services:schedule_detail', kwargs={"slug": self.name})

    class Meta:
        verbose_name = "Рабочая смена специалиста"
        verbose_name_plural = "Рабочие смены специалистов"


class Service(models.Model):
    """ Услуга """
    title = models.CharField("Название", max_length=100, default=None, blank=True)
    tagline = models.CharField("Слоган", max_length=100, default='', blank=True)
    description = models.TextField("Описание", default=None, blank=True)
    poster = models.ImageField("Постер", upload_to="services/", default=None, blank=True)
    cost = models.PositiveIntegerField("Цена", default=0, blank=True, help_text="указать сумму в гривнах")

    duration = models.PositiveSmallIntegerField("Продолжительность", default=30, blank=True,
                                                help_text="указать продолжительность в минутах")
    workers = models.ManyToManyField(Worker, verbose_name="специалист", related_name="worker", default=None,
                                     blank=True)
    service_category = models.ForeignKey(ServiceCategory, verbose_name="Категория Услуги", on_delete=models.SET_NULL,
                                         null=True, blank=True)

    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("services:service_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"


class Appointment(models.Model):
    """ Запись на приём (время, специалист, место) """
    user_name = models.CharField("Имя клиента", max_length=100)
    user_email = models.EmailField("Email", max_length=100, default=None, blank=True)  # добавил
    user_phone = models.CharField("Телефон", max_length=14, default=None, blank=True)  # добавил
    user_social = models.CharField("Соц сеть/Мессенджер", max_length=100, default=None, blank=True)  # добавил
    user_social2 = models.CharField("Соц сеть/Мессенджер (2)", max_length=100, default=None, blank=True)  # добавил
    user_social3 = models.CharField("Соц сеть/Мессенджер (3)", max_length=100, default=None, blank=True)  # добавил

    service_category = models.ForeignKey(ServiceCategory, verbose_name="Категория Услуги", on_delete=models.SET_NULL,
                                         null=True, blank=True)
    service = models.ManyToManyField(Service, verbose_name="услуга", related_name="service", default=None,
                                     blank=True)
    appointment_date = models.DateField("Дата", default=date.today, blank=True)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name="смена специалиста",
                                 related_name="schedule", default=None,
                                 blank=True)
    # location = models.ManyToManyField(Location, verbose_name="локация / кабинет", related_name="location", default=None,
    #                                  blank=True)
    # workers = models.ManyToManyField(Worker, verbose_name="специалист", related_name="worker", default=None,
    #                                  blank=True)

    description = models.TextField("Описание", default=None, blank=True)

    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("services:appointment_detail", kwargs={"slug": self.url})

    # def get_review(self):
    #     return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Запись на приём (время, специалист, место)"
        verbose_name_plural = "Записи на приём (время, специалист, место)"


class ServiceShots(models.Model):
    """ Кадры услуги """
    title = models.CharField("Заголовок", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="service_shots/")
    service = models.ForeignKey(Service, verbose_name="Услуга", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Кадры услуги"
        verbose_name_plural = "Кадры услуги"


class RatingStar(models.Model):
    """ Звезда рейтинга """
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """ Рейтинг Специалиста """
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Специалист", related_name="ratings")

    # service = models.ForeignKey(Service, on_delete=models.CASCADE, verbose_name="Услуга", related_name="ratings")

    def __str__(self):
        return f"{self.star} - {self.worker}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    """ Отзывы (на странице специалиста) """
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    worker = models.ForeignKey(Worker, verbose_name="Специалист", on_delete=models.CASCADE, related_name="reviews")

    # service = models.ForeignKey(Service, verbose_name="Услуга", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.worker}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
