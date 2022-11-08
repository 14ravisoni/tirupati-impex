from rest_framework import viewsets, filters, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from core.models import (
    JewlType, JewlStage, Jewl, Metal, JewlStageTransaction, Worker, WorkerStats, StoneJadaiTransaction, Stone
)
from core.serializers import (
    JewlTypeSerializer, JewlStageSerializer, JewlSerializer, JewlStageTransactionSerializer
)
from core.utils import (
    DataValidation, CustomHTTPResponseHandler, MetalStockUpdation, JewlIdCreation, CodeParameterValueManipulation
)


class JewlTypeViewSet(viewsets.ModelViewSet):
    queryset = JewlType.objects.all()
    serializer_class = JewlTypeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type_name']


class JewlStageViewSet(viewsets.ModelViewSet):
    queryset = JewlStage.objects.all()
    serializer_class = JewlStageSerializer


class JewlViewSet(viewsets.ModelViewSet):
    queryset = Jewl.objects.all()
    serializer_class = JewlSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^gross', '^net', '^kundan', 'jewl_id']


class JewlRetrieve(APIView):

    def get(self, request):
        jewl_stage_name = self.request.query_params.get("jewl_stage", None)
        try:
            jewl_stage = JewlStage.objects.get(stage=jewl_stage_name)
            jewls = Jewl.objects.filter(stage=jewl_stage)
        except Exception as e:
            print(e)
            return Response({'error': 'Something wrong, getting: ' + e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

        jewl_serializer = JewlSerializer(jewls, many=True)
        return Response(jewl_serializer.data, status=status.HTTP_200_OK)


class JewlGhaatAddition(APIView):

    def post(self, request):
        jewl_type_id = self.request.query_params.get("jewl_type_id", None)
        worker_id = self.request.query_params.get("worker_id", None)
        job_start_date_time = self.request.query_params.get("job_start_date_time", None)
        job_end_date_time_expected = self.request.query_params.get("job_end_date_time_expected", None)
        metal_issue_weight = self.request.query_params.get("gold_issue_weight", None)
        remarks = self.request.query_params.get("remarks", None)
        description = self.request.query_params.get("description", None)

        null_exists, null_argument_list = DataValidation.return_element_which_is_null(
            jewl_type_id, worker_id, job_start_date_time, metal_issue_weight
        )

        if null_exists:
            return CustomHTTPResponseHandler.return_error_response_if_api_parameters_are_null(null_argument_list)

        jewl_type = JewlType.objects.get(id=jewl_type_id)
        jewl_id = JewlIdCreation.get_jewl_id_from_jewl_type(jewl_type)

        # dfsfsd
        metal_debit = Metal.objects.create(
            quantity=round(float(metal_issue_weight), 3),
            is_credit=False,
            last_updated_date_time=job_start_date_time,
            description='System generated debit of metal',
            remarks='System debit for Jewel: ' + jewl_id
        )
        MetalStockUpdation.update_all_metal_stock(metal_debit.is_credit, metal_debit.quantity)

        # create jewl
        jewl_stage = JewlStage.objects.get(stage='ghaat')
        jewl = Jewl.objects.create(
            jewl_id=jewl_id,
            jewl_type=jewl_type,
            stage=jewl_stage,
            issue_weight=round(float(metal_issue_weight), 3),
        )

        # Create jewl stage transaction
        worker = Worker.objects.get(id=worker_id)
        jewl_transaction = JewlStageTransaction.objects.create(
            jewl=jewl,
            stage=jewl_stage,
            worker=worker,
            expected_finish_date_time=job_end_date_time_expected,
            description=description,
            remarks=remarks
        )

        CodeParameterValueManipulation.increment_count('current_ghaat_count')

        jewl_transaction_serializer = JewlStageTransactionSerializer(jewl_transaction)
        return Response(jewl_transaction_serializer.data, status=status.HTTP_201_CREATED)


class JewlJadaiAddition(APIView):

    def post(self, request):
        jewl_id = self.request.query_params.get("jewl_id", None)  # HR005
        # [{'stone_name': 'Diamond', 'karat': 22.45, 'quantity': 4}, {....}, {.....}]
        stone_list = self.request.query_params.get("stone_list", None)
        worker_id = self.request.query_params.get("worker_id", None)
        job_start_date_time = self.request.query_params.get("job_start_date_time", None)
        job_end_date_time_expected = self.request.query_params.get("job_end_date_time_expected", None)
        remarks = self.request.query_params.get("remarks", None)
        description = self.request.query_params.get("description", None)

        # 1. Change jewl status to jadai
        jewl_stage = JewlStage.get(stage='jadai')
        jewl = Jewl.objects.get(jewl_id=jewl_id)

        jewl.stage = jewl_stage
        jewl.last_updated_date_time = job_start_date_time
        jewl.save()

        # 2. Create a jewl stage transation
        worker = Worker.objects.get(id=worker_id)
        jewl_transaction = JewlStageTransaction.objects.create(
            jewl=jewl,
            stage=jewl_stage,
            worker=worker,
            expected_finish_date_time=job_end_date_time_expected,
            description=description,
            remarks=remarks
        )
        jewl_transaction.save()

        # 3. Change karigar attributes
        worker_stats = WorkerStats.objects.get(worker=worker)
        worker_stats.acceptance_count = worker_stats.acceptance_count + 1
        worker_stats.current_count = worker_stats.current_count + 1
        worker_stats.save()

        # 4. Change overall jewl status on the first page
        CodeParameterValueManipulation.increment_count('current_jadai_count')

        # 4. Create a StoneJadaiTransaction
        for stone_attributes in stone_list:
            stone_name = stone_attributes['stone_name']
            karat = float(stone_attributes['karat'])
            quantity = int(stone_attributes['quantity'])

            stone = Stone.objects.get(stone_name=stone_name)
            stone_jadai_transaction = StoneJadaiTransaction.objects.create(
                jewl=jewl,
                stone=stone,
                karat=karat,
                quantity=quantity
            )
            stone_jadai_transaction.save()

        return Response({'message': 'all good'}, status=status.HTTP_200_OK)
