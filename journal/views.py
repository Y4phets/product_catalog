# journal/views.py
from rest_framework import generics
from .models import Journal
from .serializers import JournalSerializer
from django_filters import rest_framework as filters


class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('cnt',)


class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
