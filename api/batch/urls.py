from django.urls import path
from . import views


urlpatterns = [
    path("batch-list-all/", views.BatchListAll, name="batch-list-all"),
    path("batch-detail/<str:record_id>/", views.BatchDetail.as_view(), name="batch-detail"),
    path("batch-create/", views.BatchCreate.as_view(), name="batch-create"),
    path("batch-update/<str:record_id>/", views.BatchUpdate.as_view(), name="batch-update"),
    path("batch-delete/<str:record_id>/", views.BatchDelete.as_view(), name="batch-delete"),
]