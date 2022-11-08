from core.models import CodeParameter


class CodeParameterValueManipulation:

    @staticmethod
    def increment_count(parameter_name):
        try:
            code_parameter = CodeParameter.objects.get(parameter_name=parameter_name)
            code_parameter.parameter_value = str(int(code_parameter.parameter_value) + 1)
            code_parameter.save()
        except Exception as e:
            print(e)
            return None

        return int(code_parameter.parameter_value)

    @staticmethod
    def decrement_count(parameter_name):
        try:
            code_parameter = CodeParameter.objects.get(parameter_name=parameter_name)
            code_parameter.parameter_value = str(int(code_parameter.parameter_value) - 1)
            code_parameter.save()
        except Exception as e:
            print(e)
            return None

        return int(code_parameter.parameter_value)
