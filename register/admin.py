from atexit import register
from django.contrib import admin
from .models import user, vehicle

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'cpf', 'enrollment', 'email', 'phone')

class VehAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'brand', 'plate', 'user')

admin.site.register(user, UserAdmin)
admin.site.register(vehicle, VehAdmin)


