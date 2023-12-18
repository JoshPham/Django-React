from rest_framework.serializers import ModelSerializer
from .models import Problem

class ReactSerializer(ModelSerializer):
    class Meta:
        model = Problem
        fields = ['question', 'answer']