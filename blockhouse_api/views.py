from django.shortcuts import render
from .models import CandleStick, LineChartData, BarChartData, PieChartData
from .serializers import CandleStickSerializer, ChartSerializer
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class CandleStickViewSet(GenericViewSet):
    queryset = CandleStick.objects.all()
    serializer_class = CandleStickSerializer
    lookup_field = 'pk'

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
 




class CharViewSet(GenericViewSet):
    serializer_class = ChartSerializer

    def get_queryset(self):
        raise NotImplementedError('Subclass must override get_queryset method')

    def list(self,request):
        queryset = self.get_queryset()
        labels = [item.label  for item in queryset]
        data = [item.value  for item in queryset]
        serializer = self.serializer_class(data={"labels": labels, "data":data})
        if serializer.is_valid():
            return Response(data=serializer.data,  status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def create(self,request):
        labels = [item['label'] for item in request.data]
        data = [item['value'] for item in request.data]
    
        serializer = self.serializer_class(data={'labels': labels, "data": data})
        if serializer.is_valid():
            for label, value in zip(labels, data):
                self.get_queryset().create(label=label, value=value)
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(data=serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


    


class LineChartViewSet(CharViewSet):     
    def get_queryset(self):
        return LineChartData.objects.all()

class BarChartViewSet(CharViewSet):
   
    def get_queryset(self):
        return BarChartData.objects.all()

class PieChartViewSet(CharViewSet):

    def get_queryset(self):
        return PieChartData.objects.all()



