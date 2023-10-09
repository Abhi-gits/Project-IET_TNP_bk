from django.contrib import admin

# Register your models here.
from api.tnp.models import Placement
from api.tnp.models import Courses

# Register your models here.
class PlacementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'company_name', 'company_email', 'company_salary', 'is_approved']
    list_filter = ['user', 'name', 'company_name', 'company_email',  'company_salary', 'is_approved']
    search_fields = ['user', 'name', 'company_name', 'company_email', 'company_salary', 'is_approved']
    list_per_page = 20

admin.site.register(Placement, PlacementAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'course_name', 'is_approved']
    list_filter = ['user', 'name', 'course_name', 'is_approved']
    search_fields = ['user', 'name', 'course_name', 'is_approved']
    list_per_page = 20

admin.site.register(Courses, CoursesAdmin)