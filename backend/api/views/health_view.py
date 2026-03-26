from datetime import datetime

from rest_framework.response import Response
from rest_framework.views import APIView


class HealthView(APIView):
    def get(self, request):
        data = {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "version": "1.0.0",
        }
        return Response(data)
