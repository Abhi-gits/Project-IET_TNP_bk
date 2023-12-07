from django.urls import path, include
from . import views

urlpatterns = [
    path("account/", include("api.account.urls")),
    # path("tnp/", include("api.tnp.urls")),
    path("placement/", include("api.placement.urls")),
    path("batch/", include("api.batch.urls")),
    path("course/", include("api.course.urls")),
]
