from django.urls import path
from . import views

urlpatterns = [
    path("", views.hanoi_view, name="hanoi_view"),
]
