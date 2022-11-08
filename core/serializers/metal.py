from rest_framework import serializers

from core.models import Metal


class MetalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metal
        fields = '__all__'
