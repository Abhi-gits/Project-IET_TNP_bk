from django.urls import path
from . import views


urlpatterns = [
    path("batch-list-all/", views.BatchListAll, name="batch-list-all"),
    path("batch-detail/<str:pk>/", views.BatchDetail, name="batch-detail"),
]