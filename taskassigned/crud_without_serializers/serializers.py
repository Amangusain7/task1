from rest_framework import serializers
from crud_without_serializers.models import WWE

class wweSerializer(serializers.ModelSerializer):
    class Meta:
        model = WWE
        fields = '__all__' 