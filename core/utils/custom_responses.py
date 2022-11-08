from rest_framework import status
from rest_framework.response import Response


class CustomHTTPResponseHandler:

    @staticmethod
    def return_error_response_if_api_parameters_are_null(list_of_null_parameters):

        string_of_null_parameters = ''

        for parameter in list_of_null_parameters:
            string_of_null_parameters = string_of_null_parameters + parameter + ', '

        error_message = 'Found null in these api parameters: ' + string_of_null_parameters[:-2]

        response = Response(
            data={"error": error_message},
            exception=True,
            status=status.HTTP_400_BAD_REQUEST,
        )
        return response
