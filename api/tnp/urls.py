from django.urls import path
from . import views


urlpatterns = [
    path('placement/', views.PlacementAPIOverview, name='placement-api-overview'),
    path('placement-list/', views.PlacementList, name='placement-list'),
    path('placement-create/', views.PlacementCreate, name='placement-create'),
    path('placement-detail/<str:pk>/', views.PlacementDetail, name='placement-detail'),
    path('placement-update/<str:pk>/', views.PlacementUpdate, name='placement-update'),
    path('placement-delete/<str:pk>/', views.PlacementDelete, name='placement-delete'),
    
    path('courses/', views.CoursesAPIOverview, name='courses-api-overview'),
    path('courses-list/', views.CoursesList, name='courses-list'),
    path('courses-create/', views.CoursesCreate, name='courses-create'),
    path('courses-detail/<str:pk>/', views.CoursesDetail, name='courses-detail'),
    path('courses-update/<str:pk>/', views.CoursesUpdate, name='courses-update'),
    path('courses-delete/<str:pk>/', views.CoursesDelete, name='courses-delete'),    
]
