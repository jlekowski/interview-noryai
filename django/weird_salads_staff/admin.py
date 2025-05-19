from django.contrib import admin

from .models import Staff


class StaffAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "date_of_birth", "iban", "bic"]
    list_filter = ["location"]


admin.site.register(Staff, StaffAdmin)
