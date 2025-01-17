

from django.contrib import admin

# Register your models here.

from .models import Chicken,Egg


### CASE STUDY 2. Admin Customization

@admin.register(Chicken)
class ChickenAdmin(admin.ModelAdmin):
    list_display = ('name','age','breed','health_status')
    list_filter=('breed','health_status')
    search_fields = ('name',)
    list_editable=('health_status',)


@admin.register(Egg)
class EggAdmin(admin.ModelAdmin):
    list_display = ('chicken','quantity','date_collected')
    list_filter = ('chicken','date_collected')




