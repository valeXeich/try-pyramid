from pyramid.config import Configurator


def includeme(config: Configurator):
    config.add_route('task', '/task/{pk}')
    config.add_route('list', '/tasks')
