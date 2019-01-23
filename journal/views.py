# journal/views.py
from rest_framework import generics
from .models import Journal
from .serializers import JournalSerializer
from django_filters.rest_framework import DjangoFilterBackend


class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('product__is_new',)


class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
