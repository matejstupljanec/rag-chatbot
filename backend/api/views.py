from datetime import datetime

from django.apps import apps
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MessageSerializer


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

        response = MessageSerializer(message)
        return Response(response.data)
