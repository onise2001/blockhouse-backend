from rest_framework import serializers

from .models import CandleStick, LineChartData, BarChartData,PieChartData


class CandleStickSerializer(serializers.ModelSerializer):
    class Meta:
        model = CandleStick
        fields = '__all__'



class ChartSerializer(serializers.Serializer):
    labels = serializers.ListField(child=serializers.CharField())
    data = serializers.ListField(child=serializers.IntegerField())