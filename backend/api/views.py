from datetime import datetime

from django.apps import apps
from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Conversation
from .serializers import ConversationSerializer, MessageSerializer


class ApiView(APIView):
    def get(self, request):
        data = {"message": "Welcome to RAG Chatbot API"}
        return Response(data)


class HealthView(APIView):
    def get(self, request):
        data = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0",
        }
        return Response(data)


class ConversationsView(APIView):
    def get(self, request):
        conversations = Conversation.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ConversationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)


class ConversationView(APIView):
    def get(self, request, id):
        conversation = get_object_or_404(Conversation, id=id)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=200)

    def patch(self, request, id):
        conversation = get_object_or_404(Conversation, id=id)

        serializer = ConversationSerializer(
            conversation, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=200)

    def delete(self, request, id):
        conversation = get_object_or_404(Conversation, id=id)
        conversation.delete()
        return Response(status=204)


class MessagesView(APIView):
    def post(self, request):
        serializer = MessageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        message = serializer.save()

        api_config = apps.get_app_config("api")
        answer = api_config.rag_pipeline.run(message.question)

        message.answer = answer
        message.answered_at = timezone.now()
        message.save()

        return Response(MessageSerializer(message).data, status=201)
