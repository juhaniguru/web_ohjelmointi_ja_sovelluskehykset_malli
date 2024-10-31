from services.json_response_handler import JsonResponseHandler
from services.user_service import UserService
from services.xml_response_handler import XmlResponseHandler


def users_service_factory(user_repo, log_repo):
    return UserService(user_repo, log_repo)


def response_handler_factory(headers):
    # luetaan requestin accept-headerista clientin haluama responsen datatyyppi (xml, json)
    # ja luodaan sopiva instanssi sevicesta
    _accept_header = headers.get('Accept', 'application/json')

    # molemmat responsehandlerit (jsonresponsehandler ja xmlresponsehandler) sisältävät metodin send_response
    # joissa määritellään se, miten data käsitellään (xml ja json pitää käsitellä eri tavalla)

    if 'application/json' in _accept_header:
        return JsonResponseHandler()
    elif 'application/xml' in _accept_header:
        return XmlResponseHandler()
    else:
        # jos mikään accept-headerin arvo ei täsmää, käytetään oletuksena jsonia
        return JsonResponseHandler()
