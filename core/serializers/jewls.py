from rest_framework import serializers

from core.models import (
    JewlType, JewlStage, Jewl, JewlStageTransaction
)
from core.serializers import WorkerSerializer


class JewlTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = JewlType
        fields = '__all__'


class JewlStageSerializer(serializers.ModelSerializer):

    class Meta:
        model = JewlStage
        fields = '__all__'


class JewlSerializer(serializers.ModelSerializer):
    jewl_type = JewlTypeSerializer(read_only=True)
    stage = JewlStageSerializer(read_only=True)

    class Meta:
        model = Jewl
        fields = '__all__'


class JewlStageTransactionSerializer(serializers.ModelSerializer):
    jewl = JewlSerializer(read_only=True)
    stage = JewlStageSerializer(read_only=True)
    worker = WorkerSerializer(read_only=True)

    class Meta:
        model = JewlStageTransaction
        fields = '__all__'
