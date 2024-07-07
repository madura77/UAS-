from django.urls import path
from . import views

urlpatterns = [
    path("Perpus/", views.PerpusListCreate.as_view(), name="Perpus-view-create")
]

urlpatterns = [
    path("Admin/", views.AdminListCreate.as_view(), name="Admin-view-create")
]