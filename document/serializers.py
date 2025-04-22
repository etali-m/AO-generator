from rest_framework import serializers
from .models import TypeMarche

class TypeMarcheSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeMarche
        fields = ['nom', 'description', 'image_garde']