from settings import INSTALLED_APPS
from functools import reduce


def get_server_actions():
    return reduce(
        lambda value, item: value + getattr(item, 'action_names', []),
        reduce(
            lambda value, item: value + [getattr(item, 'actions', [])],
            reduce(
                lambda value, item: value + [__import__(f'{item}.actions')],
                INSTALLED_APPS,
                []
            ),
            []
        ),
        []
    )


def resolve(action_name, actions=None):
    actions_list = actions or get_server_actions()
    actions_map = {
        action.get('action'): action.get('controller')
        for action in actions_list
    }
    return actions_map.get(action_name)
