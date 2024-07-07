from rest_framework import serializers
from .models import Perpus
from .models import Admin
from .models import Peminjam


class PerpusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perpus
        fields = ["id", "title", "content", "published_date",]

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin 
        fields = ["id", "title", "content", "published_date",]        

class PeminjamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peminjam
        fields = ["id", "title", "content", "published_date",]