from django.contrib import admin

from .models import RakJopi

@admin.register(RakJopi)
class RakJopiAdmin(admin.ModelAdmin):
    pass
