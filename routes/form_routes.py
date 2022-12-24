from aws_cdk.aws_apigateway import RestApi

from ..stacks.form_stack import FormStack
from ..utils.constants import http_method


def form_routes(api: RestApi, form_stack: FormStack):
    """
    A function that create form routes using API Gateway.

    :param api: aws_cdk.aws_apigateway.RestApi
    :param form_stack: FormStack
    :return: None
    """
    forms = api.root.add_resource("forms")
    form = forms.add_resource("{form_id}")

    # api/forms
    forms.add_method(http_method.GET, form_stack.form_list_function)
    forms.add_method(http_method.POST, form_stack.form_create_function)
    # api/forms/{form_id}
    form.add_method(http_method.GET, form_stack.form_get_function)
    form.add_method(http_method.PUT, form_stack.form_update_function)
    form.add_method(http_method.PATCH, form_stack.form_update_function)
    form.add_method(http_method.DELETE, form_stack.form_delete_function)
