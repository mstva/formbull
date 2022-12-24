from collections import namedtuple

FormResponse = namedtuple('FormResponse', 'statusCode body')


def form_list(event, context):
    """
    A function that return a list of forms.

    :param event:
    :param context:
    :return: FormResponse
    """
    return FormResponse(
        statusCode=200,
        body="form list"
    )._asdict()


def form_create(event, context):
    """
    A function that create a form.

    :param event:
    :param context:
    :return: FormResponse
    """
    return FormResponse(
        statusCode=200,
        body="create form"
    )._asdict()


def form_get(event, context):
    """
    A function that return one form based on form_id.

    :param event:
    :param context:
    :return: FormResponse
    """
    return FormResponse(
        statusCode=200,
        body="get form"
    )._asdict()


def form_update(event, context):
    """
    A function that update a form.

    :param event:
    :param context:
    :return: FormResponse
    """
    return FormResponse(
        statusCode=200,
        body="update form"
    )._asdict()


def form_delete(event, context):
    """
    A function that delete a form.

    :param event:
    :param context:
    :return: FormResponse
    """
    return FormResponse(
        statusCode=200,
        body="delete form"
    )._asdict()
