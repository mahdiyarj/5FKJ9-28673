from django.contrib import admin

from . import models


@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    model = models.Restaurant


@admin.register(models.User)
class RestaurantAdmin(admin.ModelAdmin):
    model = models.User
