from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Conversation
from ..serializers import ConversationSerializer


class ConversationsView(APIView):
    def get(self, request):
        conversations = Conversation.objects.all()
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ConversationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if not serializer.validated_data.get("name"):
            count = Conversation.objects.count()
            conversation_name = f"Razgovor #{count + 1}"
            serializer.save(name=conversation_name)
        else:
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
