from rest_framework.decorators import api_view
from rest_framework.response import Response

from core.models import CodeParameter


@api_view(['GET'])
def get_all_current_jewl_count(request):
    if request.method == 'GET':
        cp_current_ghaat_count = CodeParameter.objects.get(parameter_name='current_ghaat_count')
        cp_current_jadai_count = CodeParameter.objects.get(parameter_name='current_jadai_count')
        cp_current_puai_count = CodeParameter.objects.get(parameter_name='current_puai_count')

        return Response({
            'current_ghaat_count': cp_current_ghaat_count.parameter_value,
            'current_jadai_count': cp_current_jadai_count.parameter_value,
            'current_puai_count': cp_current_puai_count.parameter_value,
        })
