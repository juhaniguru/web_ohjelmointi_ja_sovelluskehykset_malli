from repositories.repository_factory import users_repository_factory


def get_repository(name):
    def decorator(route_handler_func):
        def wrapper(con, *args, **kwargs):
            if name == 'users':
                repo = users_repository_factory(con)
                return route_handler_func(repo, *args, **kwargs)

        return wrapper
    return decorator


