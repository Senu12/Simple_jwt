from django.contrib import admin
from .models import Stocktick

# Register your models here.


@admin.register(Stocktick)
class StocktickAdmin(admin.ModelAdmin):
    list_display = ['id', 'plant', 'godown', 'our_lot', 'recd_date', 'types', 'garden',
                    'grade', 'inv_no', 'cases', 'kg', 'net_kg', 'row_no', 'remarks', 'status']
