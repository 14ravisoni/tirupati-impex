from core.models import JewlType, CodeParameter


class JewlIdCreation:

    @staticmethod
    def get_jewl_id_from_jewl_type(jewl_type: JewlType):

        parameter_name = 'jewl_type_{}_count'.format(jewl_type.type_name)
        cp_jewl_count = CodeParameter.objects.get(parameter_name=parameter_name)
        cp_jewl_count.parameter_value = str(int(cp_jewl_count.parameter_value) + 1)
        cp_jewl_count.save()

        jewl_id = jewl_type.type_code + cp_jewl_count.parameter_value.zfill(3)
        return jewl_id

