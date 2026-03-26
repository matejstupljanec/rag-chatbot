from rest_framework.response import Response
from rest_framework.views import APIView


class ApiView(APIView):
    def get(self, request):
        data = {"message": "Welcome to RAG Chatbot API"}
        return Response(data)
