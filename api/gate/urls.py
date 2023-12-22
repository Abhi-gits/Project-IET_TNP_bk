from django.urls import path
from . import views


urlpatterns = [
    path("gate-list-all/", views.GateListAll, name="gate-list-all"),
    path("gate-list-approved/", views.GateListApproved, name="gate-list-approved"),
    path("gate-create/", views.GateCreate.as_view(), name="gate-create"),
    path("gate-detail/<str:record_id>/", views.GateDetail.as_view(), name="gate-detail"),
    path("gate-update/<str:record_id>/", views.GateUpdate.as_view(), name="gate-update"),
    path("gate-delete/<str:record_id>/", views.GateDelete.as_view(), name="gate-delete"),
]