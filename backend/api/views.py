from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView
from api.services.rag_service import RAGService

# Create your views here.


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


class QuestionsView(APIView):
    def post(self, request):
        question = request.data.get("question")
        answer = RAGService.ask(question)
        data = {"answer": answer}
        return Response(data)
