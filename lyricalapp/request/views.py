from django.shortcuts import render
import django_filters
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny, IsAdminUser

from .serializers import RequestSerializer
from .models import Request


class RequestViewSet(viewsets.ModelViewSet):
    serializer_class = RequestSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = (IsAdminUser,)
    queryset = Request.objects.all()
    ordering_fields = ['date']
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend, SearchFilter, OrderingFilter)
