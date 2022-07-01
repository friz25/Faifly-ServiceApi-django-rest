from django import forms
from django.contrib import admin, messages
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
# from modeltranslation.admin import TranslationAdmin #удалено

from .models import ServiceCategory, Worker, Location, Time, TimeLocation, Schedule, Service, Appointment, ServiceShots, RatingStar, Rating, Review

admin.site.sit_title = "Faifly-ServiceApi-django-rest"
admin.site.site_header = "Faifly-ServiceApi-django-rest"

admin.site.register(Time)
admin.site.register(RatingStar)

# admin.site.register(ServiceCategory)
# admin.site.register(Worker)
# admin.site.register(Location)
# admin.site.register(TimeLocation)
# admin.site.register(Schedule)
# admin.site.register(Service)
# admin.site.register(Appointment)
# admin.site.register(ServiceShots)
# admin.site.register(Rating)
# admin.site.register(Review)

from ckeditor_uploader.widgets import CKEditorUploadingWidget

class ServiceAdminForm(forms.ModelForm):
    """GOOD

    Текстовый редактор CKEditor"""
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())  # переименовано
    # description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget()) # удалено

    class Meta:
        model = Service
        fields = '__all__'

class AppointmentAdminForm(forms.ModelForm):
    """GOOD

    Текстовый редактор CKEditor"""
    description = forms.CharField(label="Описание", widget=CKEditorUploadingWidget())  # переименовано
    # description_en = forms.CharField(label="Description", widget=CKEditorUploadingWidget()) # удалено

    class Meta:
        model = Appointment
        fields = '__all__'
"""################################ ACTOR ######################################
"""
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    """GOOD

    Специалисты"""
    list_display = ("name", "speciality", "email",  "phone", "get_image", "draft")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src={obj.image.url} width="100" height="120">')
        except:
            return ""
    get_image.short_descriprion = "Изображение"

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """ GOOD

    Локация / Кабинет """
    list_display = ("name", "floor", "adress",  "speciality", "working_hours_start", "working_hours_end", "get_image")
    readonly_fields = ("get_image", )

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src={obj.image.url} width="100" height="120">')
        except:
            return ""
    get_image.short_descriprion = "Изображение"

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    """GOOD

    Рабочие смены специалиста"""
    list_display = ("name", "draft") #, "get_image", "timelocation",
    #readonly_fields = ("get_image", )

    # def get_image(self, obj):
    #     try:
    #         return mark_safe(f'<img src={obj.image.url} width="100" height="120">')
    #     except:
    #         return ""
    # get_image.short_descriprion = "Изображение"
"""################################ ACTOR ######################################
"""

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """GOOD

    Рейтинг Специалиста"""
    list_display = ("star", "worker", "ip")
@admin.register(TimeLocation)
class TimeLocationAdmin(admin.ModelAdmin):
    """GOOD

    ВремяМесто"""
    list_display = ("day_of_week", "time", "location", "worker", "ip")
"""################################ RATING ######################################
"""
@admin.register(ServiceShots)
class ServiceShotsAdmin(admin.ModelAdmin):
    """GOOD

    Кадры услуги """
    list_display = ("title", "service", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src={obj.image.url} width="150" height="100">')
        except:
            return ""
    get_image.short_description = "Изображение"
"""################################ ServiceShots ######################################
"""
@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    """GOOD

    Категории Услуги"""
    # fields = ['name', 'rating']
    # exclude = ['slug']
    # readonly_fields = ['year']
    prepopulated_fields = {'url': ('name',)}
    # filter_horizontal = ['directors', 'actors', 'genres']
    # filter_vertical = ['actors']
    list_display = ['id', 'name', 'description']
    list_display_links = ['name']
    list_editable = ['description']
    # ordering = ['rating', 'name']
    list_per_page = 10
    # actions = ['set_dollars', 'set_euro']
    search_fields = ['name', 'description']  # + строка поиска
    # list_filter = ['title', 'year', 'country', 'budget', 'draft']  # +фильтры справа
"""################################ ServiceCategory ######################################
"""
class ReviewInline(admin.TabularInline):
    """GOOD

    Отзывы (на странице специалиста)"""
    model = Review
    extra = 1
    readonly_fields = ['parent', 'name', 'email']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """GOOD

    Отзывы  (на странице специалиста)"""
    # fields = ['name', 'rating']
    # exclude = ['parent']
    # readonly_fields = ['parent', 'name', 'email']
    # prepopulated_fields = {'url': ('title',)}
    # filter_horizontal = ['movie']
    # filter_vertical = ['actors']
    list_display = ['name', 'email', 'text', 'parent', 'worker', 'id']
    list_editable = ['email', 'text', 'worker']
    # ordering = ['rating', 'name']
    list_per_page = 10
    # actions = ['set_dollars', 'set_euro']
    search_fields = ['name', 'text']  # + строка поиска
    # list_filter = ['title', 'year', 'country', 'budget', 'draft']  # +фильтры справа

class ServiceShotsInline(admin.TabularInline):
    """GOOD

    Кадры Услуги (на странице услуги)"""
    model = ServiceShots
    extra = 1
    readonly_fields = ['get_image']

    def get_image(self, obj):
        try:
            return mark_safe(f'<img src={obj.image.url} width="150" height="100">')
        except:
            return ""
    get_image.short_description = "Изображение"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """GOOD

     Услуга """
    # fields = ['name', 'rating']
    # exclude = ['slug']
    form = ServiceAdminForm #CKEditor
    readonly_fields = ['get_poster_image']
    # prepopulated_fields = {'url': ('title', )}
    filter_horizontal = ['workers']
    # filter_vertical = ['actors']
    list_display = ['title', 'cost', 'duration', 'service_category', 'draft']
    list_filter = ['service_category']
    list_editable = ['duration', 'cost']
    # ordering = ['rating', 'name']
    list_per_page = 10
    actions = ['unpublish', 'publish']
    search_fields = ['title', 'tagline', 'service_category__name']  # + строка поиска
    # list_filter = ['title', 'year', 'country', 'budget', 'draft']  # +фильтры справа
    inlines = [ServiceShotsInline] #[, ReviewInline] список [комментов, кадров из фильма] к фильму
    save_on_top = True
    save_as = True
    # fields = (("budget", "fees_in_usa", "fees_in_world"),)
    fieldsets = (
        (None, {
            "fields": (('title', 'tagline'),)
        }),
        (None, {
            "fields": (('description', 'poster', 'get_poster_image'),)
        }),
        (None, {
            "fields": (('duration', 'cost'),)
        }),
        (None, {
            "fields": (('workers'),)
        }),
        (None, {
            "fields": (('service_category'),)
        }),
        (None, {
            "fields": (('url', 'draft'),)
        }),
    )

    def get_poster_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="120">')

    get_poster_image.short_description = "Постер"

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f'{message_bit}')

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )#у user'a должны быть права на "изменение"

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change', )#у user'a должны быть права на "изменение"
"""################################ Service (Movie) ######################################
"""
@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    """GOOD

      Запись на приём (время, специалист, место)  """
    # fields = ['name', 'rating']
    # exclude = ['slug']
    form = AppointmentAdminForm #CKEditor
    # prepopulated_fields = {'url': ('title', )}
    filter_horizontal = ['service'] #, 'schedule'
    # filter_vertical = ['actors']
    list_display = ['user_name', 'user_email', 'user_phone', 'appointment_date', 'draft']
    list_filter = ['service__service_category', 'appointment_date']
    # list_editable = ['title']
    # ordering = ['rating', 'name']
    list_per_page = 10
    actions = ['unpublish', 'publish']
    search_fields = ['user_name', 'user_email', 'user_phone', 'appointment_date', 'service__title']  # + строка поиска
    # list_filter = ['title', 'year', 'country', 'budget', 'draft']  # +фильтры справа

    # inlines = [AppointmentShotsInline, ReviewInline] #список [комментов, кадров из фильма] к фильму

    save_on_top = True
    save_as = True
    # fields = (("budget", "fees_in_usa", "fees_in_world"),)
    fieldsets = (
        (None, {
            "fields": (('user_name',),)
        }),
        (None, {
            "fields": (('user_email', 'user_phone'),)
        }),
        ("Ваши соцсети", {
            "classes": ("collapse",),
            "fields": (('user_social', 'user_social2', 'user_social3'),)
        }),
        (None, {
            "fields": (('service_category', 'service'),)
        }),
        (None, {
            "fields": (('appointment_date', 'schedule'),)
        }),
        ("Ваш Комментарий", {
            "classes": ("collapse",),
            "fields": (('description'),)
        }),
        (None, {
            "fields": (('url', 'draft'),)
        }),
    )

    def unpublish(self, request, queryset):
        """Снять с публикации"""
        row_update = queryset.update(draft=True)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f'{message_bit}')

    def publish(self, request, queryset):
        """Опубликовать"""
        row_update = queryset.update(draft=False)
        if row_update == 1:
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request, f'{message_bit}')

    publish.short_description = "Опубликовать"
    publish.allowed_permissions = ('change', )#у user'a должны быть права на "изменение"

    unpublish.short_description = "Снять с публикации"
    unpublish.allowed_permissions = ('change', )#у user'a должны быть права на "изменение"
"""################################ Appointment (Movie) ######################################
"""

