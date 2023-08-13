from django.contrib import admin

# Register your models here.
from api.tnp.models import Placement
from api.tnp.models import Courses

# Register your models here.
class PlacementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'company_name', 'company_email', 'company_salary', 'company_location', 'company_category', 'company_status', 'is_approved']
    list_filter = ['user', 'company_name', 'company_email',  'company_salary', 'company_location', 'company_category', 'company_status',  'is_approved']
    search_fields = ['user', 'company_name', 'company_email', 'company_salary', 'company_location', 'company_category', 'company_status',  'is_approved']
    list_per_page = 20

admin.site.register(Placement, PlacementAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'course_name', 'course_status', 'is_approved']
    list_filter = ['user', 'course_name', 'course_status', 'is_approved']
    search_fields = ['user', 'course_name', 'course_status', 'is_approved']
    list_per_page = 20

admin.site.register(Courses, CoursesAdmin)