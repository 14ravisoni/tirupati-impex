from core.models import CodeParameter


class MetalStockUpdation:

    @staticmethod
    def update_all_metal_stock(is_credit, quantity):
        cp_current_metal_stock = CodeParameter.objects.get(parameter_name='current_metal_stock')
        cp_total_stock_intake = CodeParameter.objects.get(parameter_name='total_metal_stock_intake')
        cp_total_stock_outtake = CodeParameter.objects.get(parameter_name='total_metal_stock_outtake')

        if is_credit:
            cp_total_stock_intake.parameter_value = str(
                round(float(cp_total_stock_intake.parameter_value) + quantity, 3)
            )
            cp_current_metal_stock.parameter_value = str(
                round(float(cp_current_metal_stock.parameter_value) + quantity, 3)
            )
        else:
            cp_total_stock_outtake.parameter_value = str(
                round(float(cp_total_stock_outtake.parameter_value) + quantity, 3)
            )
            cp_current_metal_stock.parameter_value = str(
                round(float(cp_current_metal_stock.parameter_value) - quantity, 3)
            )

        cp_current_metal_stock.save()
        cp_total_stock_intake.save()
        cp_total_stock_outtake.save()
