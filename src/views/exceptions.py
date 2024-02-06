from pyramid.view import exception_view_config
from pyramid.exceptions import HTTPNotFound, HTTPBadRequest
from pyramid.request import Request
from pyramid.response import Response


@exception_view_config(HTTPNotFound, renderer='json')
def does_not_exist_response(exc: HTTPNotFound, request: Request):
    return Response(json_body={"error": exc.detail}, status=404)


@exception_view_config(HTTPBadRequest, renderer='json')
def bad_request_handler(exc: HTTPBadRequest, request: Request):
    return Response(json_body={"error": exc.detail}, status=400)