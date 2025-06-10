from rest_framework import serializers
from .models import *

class AAOSerializer(serializer.ModelSerializer):
    class Meta:
        model = AvisAppelOffre
        fiedls = '__all__'