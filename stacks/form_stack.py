from constructs import Construct

from ..functions import form_functions as forms_functions
from ..utils.helpers import create_lambda_function


class FormStack:

    def __init__(self, scope: Construct) -> None:
        _form_functions = forms_functions.__name__.split(".")[1]
        _form_list_handler = f"{_form_functions}.{forms_functions.form_list.__name__}"
        _form_create_handler = f"{_form_functions}.{forms_functions.form_create.__name__}"
        _form_get_handler = f"{_form_functions}.{forms_functions.form_get.__name__}"
        _form_update_handler = f"{_form_functions}.{forms_functions.form_update.__name__}"
        _form_delete_handler = f"{_form_functions}.{forms_functions.form_delete.__name__}"

        self.form_list_function = create_lambda_function(scope, _form_list_handler)
        self.form_create_function = create_lambda_function(scope, _form_create_handler)
        self.form_get_function = create_lambda_function(scope, _form_get_handler)
        self.form_update_function = create_lambda_function(scope, _form_update_handler)
        self.form_delete_function = create_lambda_function(scope, _form_delete_handler)
