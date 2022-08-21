from django.contrib import admin
from .models import Calender
# Register your models here.

# class CalenderAdmin(admin.ModelAdmin):
#     def has_add_permission(self, request):
#         return False
#     def has_delete_permission(self, request, obj=None):
#         return False

admin.site.register(Calender)
