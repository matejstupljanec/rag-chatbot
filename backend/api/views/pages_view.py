from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from ..models import Page
from ..serializers import PageSerializer


class PagesView(APIView):
    def get(self, request):
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = PageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=201)


class PageView(APIView):
    def get(self, request, id):
        page = get_object_or_404(Page, id=id)
        serializer = PageSerializer(page)
        return Response(serializer.data, status=200)

    def delete(self, request, id):
        page = get_object_or_404(Page, id=id)
        page.delete()
        return Response(status=204)
