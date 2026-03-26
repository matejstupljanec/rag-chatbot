from django.apps import apps
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Conversation, Message
from ..serializers import MessageSerializer


class MessagesView(APIView):
    def get(self, request, conversation_id):
        conversation = get_object_or_404(Conversation, id=conversation_id)
        messages = conversation.messages.all()

        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, conversation_id):
        conversation = get_object_or_404(Conversation, id=conversation_id)

        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = serializer.save(conversation=conversation)

        api_config = apps.get_app_config("api")
        answer = api_config.rag_pipeline.run(message.question)

        message.answer = answer
        message.answered_at = timezone.now()
        message.save()

        serializer = MessageSerializer(message)
        return Response(serializer.data, status=201)


class MessageView(APIView):
    def get(self, request, conversation_id, message_id):
        conversation = get_object_or_404(Conversation, id=conversation_id)
        message = get_object_or_404(Message, id=message_id, conversation=conversation)

        serializer = MessageSerializer(message)
        return Response(serializer.data, status=200)


class MessageLikeView(APIView):
    def patch(self, request, conversation_id, message_id):
        conversation = get_object_or_404(Conversation, id=conversation_id)
        message = get_object_or_404(Message, id=message_id, conversation=conversation)

        message.liked_at = timezone.now()
        message.disliked_at = None
        message.save()

        serializer = MessageSerializer(message)
        return Response(serializer.data, status=200)


class MessageDislikeView(APIView):
    def patch(self, request, conversation_id, message_id):
        conversation = get_object_or_404(Conversation, id=conversation_id)
        message = get_object_or_404(Message, id=message_id, conversation=conversation)

        message.disliked_at = timezone.now()
        message.liked_at = None
        message.save()

        serializer = MessageSerializer(message)
        return Response(serializer.data, status=200)
