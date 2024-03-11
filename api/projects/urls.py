from django.urls import path
from . import views


urlpatterns = [
    path("projects-list-all/", views.ProjectsListAll, name="projects-list-all"),
    path("projects-list-approved/", views.ProjectsListApproved, name="projects-list-approved"),
    path("projects-create/", views.ProjectsCreate.as_view(), name="projects-create"),
    path("projects-detail/<str:record_id>/", views.ProjectsDetail.as_view(), name="projects-detail"),
    path("projects-update/<str:record_id>/", views.ProjectsUpdate.as_view(), name="projects-update"),
    path("projects-delete/<str:record_id>/", views.ProjectsDelete.as_view(), name="projects-delete"),
]