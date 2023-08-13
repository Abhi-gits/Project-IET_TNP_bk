from django.contrib import admin

# Register your models here.
from api.placement.models import Placement

# Register your models here.
class PlacementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at']
    list_filter = ['user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at']
    search_fields = ['user', 'company_name', 'company_email', 'company_website', 'company_address', 'company_phone', 'company_salary', 'company_location', 'company_category', 'company_status', 'created_at', 'updated_at']
    list_per_page = 20

admin.site.register(Placement, PlacementAdmin)
