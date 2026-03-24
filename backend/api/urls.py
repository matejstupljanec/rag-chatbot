from django.urls import path

from .views import ApiView, HealthView, MessagesView, ConversationsView

app_name = "api"

urlpatterns = [
    path("", ApiView.as_view()),
    path("health", HealthView.as_view()),
    path("messages", MessagesView.as_view()),
    path("conversations", ConversationsView.as_view())
]
