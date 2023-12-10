from django.urls import path
from . import views


urlpatterns = [
    path("course-list-all/", views.CourseListAll, name="course-list-all"),
    path("course-list-approved/", views.CourseListApproved, name="course-list-approved"),
    path("course-create/", views.CourseCreate.as_view(), name="course-create"),
    path("course-detail/<str:record_id>/", views.CourseDetail.as_view(), name="course-detail"),
    path("course-update/<str:record_id>/", views.CourseUpdate.as_view(), name="course-update"),
    path("course-delete/<str:record_id>/", views.CourseDelete.as_view(), name="course-delete"),
]