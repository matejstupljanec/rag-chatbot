from django.urls import path

from .views import ApiView, HealthView, MessagesView

app_name = "api"

urlpatterns = [
    path("", ApiView.as_view()),
    path("health", HealthView.as_view()),
    path("messages", MessagesView.as_view())
]
