from django.shortcuts import render
from rest_framework import generics
from .models import Perpus, Admin, Peminjam
from .serializers import PerpusSerializer
from .serializers import AdminSerializer
from .serializers import PeminjamSerializer


class PerpusListCreate(generics.ListCreateAPIView):
    queryset = Perpus.objects.all
    serializer_class = PerpusSerializer

class AdminListCreate(generics.ListCreateAPIView):
    queryset = Admin.objects.all
    serializer_class = AdminSerializer

class PeminjamListCreate(generics.ListCreateAPIView):
    queryset = Peminjam.objects.all
    serializer_class = PeminjamSerializer