from pyramid.view import view_config
from pyramid.exceptions import HTTPNotFound
from pyramid.request import Request
from pyramid.response import Response


@view_config(context=HTTPNotFound, renderer='json')
def does_not_exsist_response(exc: HTTPNotFound, request: Request):
    return Response(json_body={"error": exc.detail}, status=404)