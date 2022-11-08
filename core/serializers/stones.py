from rest_framework import serializers

from core.models import Stone, StoneJadaiTransaction


class StoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stone
        fields = '__all__'


class StoneJadaiTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StoneJadaiTransaction
        fields = '__all__'
