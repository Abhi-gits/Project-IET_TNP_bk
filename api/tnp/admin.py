from django.contrib import admin

# Register your models here.
from api.tnp.models import Placement, Courses, Batch

# Register your models here.
class BatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'starting_year', 'ending_year']
    list_filter = ['starting_year', 'ending_year']
    search_fields = ['starting_year', 'ending_year']
    list_per_page = 20
    
admin.site.register(Batch, BatchAdmin)
class PlacementAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'student_name', 'student_branch', 'student_roll_no', 'student_batch', 'company_name', 'student_salary', 'position_offered', 'company_offer_letter', 'remarks', 'is_approved']
    list_filter = ['user', 'student_name', 'company_name',  'student_salary', 'is_approved']
    search_fields = ['user', 'student_name', 'company_name', 'student_salary', 'is_approved']
    list_per_page = 20

admin.site.register(Placement, PlacementAdmin)


class CoursesAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'student_name', 'course_name', 'is_approved']
    list_filter = ['user', 'student_name', 'course_name', 'is_approved']
    search_fields = ['user', 'student_name', 'course_name', 'is_approved']
    list_per_page = 20

admin.site.register(Courses, CoursesAdmin)