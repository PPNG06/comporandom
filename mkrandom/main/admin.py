from django.contrib import admin
from .models import Character, Vehicle, Tire, Glider, Compo
# Register your models here.
class CompoAdmin(admin.ModelAdmin):
    list_display = ['char','veh','tire','glider']

admin.site.register(Character)
admin.site.register(Vehicle)
admin.site.register(Tire)
admin.site.register(Glider)
admin.site.register(Compo, CompoAdmin)
