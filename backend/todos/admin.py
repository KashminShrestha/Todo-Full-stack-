from django.contrib import admin
from .models import (
    Todo,
)

# Register your models here.


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "created_at",
        "updated_at",
    ]
    list_search = [
        "title",
    ]
    list_filter = [
        "created_at",
        "updated_at",
    ]
