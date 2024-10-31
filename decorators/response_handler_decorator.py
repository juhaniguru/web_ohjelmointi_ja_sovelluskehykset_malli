from flask import request

from services.service_factory import response_handler_factory


def get_response_handler(route_handler_func):
    def wrapper(service, *args, **kwargs):
        # tässä dekoraattorissa luodaan response_handler_servicesta instanssi
         #niit on kaksi (json_resonse_handler ja xml_reponse_handler)

        response_handler = response_handler_factory(request.headers)
        return route_handler_func(service, response_handler, *args, **kwargs)
    return wrapper