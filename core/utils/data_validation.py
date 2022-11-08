class DataValidation:

    @staticmethod
    def return_element_which_is_null(*argv):
        null_argument_list = []

        for arg in argv:
            if arg is None:
                null_argument_list.append(arg)

        null_exists = False if len(null_argument_list) == 0 else True

        return null_exists, null_argument_list
