from django.urls import path

from .views import (
    ApiView,
    ConversationsView,
    ConversationView,
    HealthView,
    MessageDislikeView,
    MessageLikeView,
    MessagesView,
    MessageView,
    PagesView,
    PageView
)

app_name = "api"

urlpatterns = [
    path("", ApiView.as_view()),
    path("health", HealthView.as_view()),
    path("conversations", ConversationsView.as_view()),
    path("conversations/<int:id>", ConversationView.as_view()),
    path("conversations/<int:conversation_id>/messages", MessagesView.as_view()),
    path("conversations/<int:conversation_id>/messages/<int:message_id>", MessageView.as_view()),
    path("conversations/<int:conversation_id>/messages/<int:message_id>/like", MessageLikeView.as_view()),
    path("conversations/<int:conversation_id>/messages/<int:message_id>/dislike", MessageDislikeView.as_view()),
    path("pages", PagesView.as_view()),
    path("pages/<int:id>", PageView.as_view())

]
