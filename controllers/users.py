from flask import jsonify
from pip._internal import models


from decorators.db_connection import get_db_connection

from decorators.response_handler_decorator import get_response_handler
from decorators.service_decorator import service_decorator




@get_db_connection
@service_decorator('users')
@get_response_handler
def get_all_users(user_service, response_handler):
    # kun käytämme service-patternia,
    # servicea kutsutaan controllerista
    # ja servicen alle kätketään kaikki muu logiikka
    # tässä tapauksessa kaksi eri repoa

    # näin mahdollinen monimutkainen logiikka pysyy piilossa ja poissa controllerista
    users = user_service.get_all()

    res_data = response_handler.send_response(users)
    return res_data
