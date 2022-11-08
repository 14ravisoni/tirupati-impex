from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from core.serializers import MetalSerializer
from core.models import Metal, CodeParameter
from core.utils import MetalStockUpdation


@api_view(['GET', 'POST'])
def credit_debit_metal(request):
    if request.method == 'GET':
        metals = Metal.objects.all()
        serializer = MetalSerializer(metals, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':

        serializer = MetalSerializer(data=request.data)
        if serializer.is_valid():

            is_credit = bool(request.data['is_credit'])
            quantity = round(float(request.data['quantity']), 3)
            MetalStockUpdation.update_all_metal_stock(is_credit, quantity)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_current_metal_stock(request):
    if request.method == 'GET':
        cp_current_metal_stock = CodeParameter.objects.get(parameter_name='current_metal_stock')
        return Response(cp_current_metal_stock.parameter_value)
