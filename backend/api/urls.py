from django.urls import path

from .views import ApiView, HealthView, QuestionsView

app_name = "api"

urlpatterns = [
    path("", ApiView.as_view()),
    path("health", HealthView.as_view()),
    path("questions", QuestionsView.as_view())
]
