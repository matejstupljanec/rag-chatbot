from django.urls import path

from .views import ApiView, HealthView, MessagesView, ConversationsView, ConversationView

app_name = "api"

urlpatterns = [
    path("", ApiView.as_view()),
    path("health", HealthView.as_view()),
    path("messages", MessagesView.as_view()),
    path("conversations", ConversationsView.as_view()),
    path("conversations/<int:id>", ConversationView.as_view()),
]
