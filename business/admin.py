from django.contrib import admin
from .models import Value

# Register your models here.
class ValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'timestamp')
    list_filter = ('timestamp', 'id')

admin.site.register(Value, ValueAdmin)