from django.contrib import admin
from .models import Value, DiscardedValue

# Register your models here.
class ValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'timestamp')
    list_filter = ('timestamp', 'id')

class DiscardedValueAdmin(admin.ModelAdmin):
    list_display = ('value', 'timestamp', 'reasons')
    list_filter = ('timestamp', 'reasons')


admin.site.register(Value, ValueAdmin)
admin.site.register(DiscardedValue, DiscardedValueAdmin)