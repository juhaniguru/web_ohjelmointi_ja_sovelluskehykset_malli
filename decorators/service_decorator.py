from repositories.repository_factory import users_repository_factory, log_repository_factory
from services.service_factory import users_service_factory


# tässä määritellään parametrillä, mikä service luodaan
def service_decorator(name):
    def decorator(route_handler):
        # tässä tulee get_db_conn-dekoraattorista ensimmäisenä parametrinä tietokantayhteys
        def wrapper(con, *args, **kwargs):
            service = None
            if name == 'users':
                # käytetään factory_patternia luomaan users_repository
                # se saa dependencyna tietokantayhteyden
                user_repo = users_repository_factory(con)
                # samoin log repo
                log_repo = log_repository_factory(con)
                # kun molemmat dependencyt (repot) on luotu, voidaan luoda user_service
                # jolle annetaan constructor injectionin avulla molemmat repot
                service = users_service_factory(user_repo, log_repo)
            return route_handler(service, *args, **kwargs)
        return wrapper
    return decorator

