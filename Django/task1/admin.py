from django.contrib import admin
from .models import *

admin.site.register(Buyer)

# Register your models here.

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ("title", "cost", "description",)
    #fields = [("title", "cost"),"description",]
    search_fields = ("title",)
    list_filter = ("cost","age_limited")
    fieldsets = (
        ("info",{
            "fields":
                ("title", "cost")
        }),
        ("footer",{
            'fields':
                ("size","description","age_limited")
        })
    )