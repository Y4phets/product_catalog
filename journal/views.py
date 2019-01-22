# journal/views.py
from rest_framework import generics
from .models import Journal
from .serializers import JournalSerializer


class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer


class JournalNewList(generics.ListAPIView):
    queryset = Journal.objects.filter(product__is_new=True)
    serializer_class = JournalSerializer


class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer
