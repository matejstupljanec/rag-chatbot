from django.urls import path

from .views import ApiView, HealthView

app_name = "api"

urlpatterns = [
    path("", ApiView.as_view(), name=""),
    path("health/", HealthView.as_view(), name="health")
]
