from .controllers import get_echo

# TODO 1: переменная action_names может быть словарем {'action_name_1': action 1, 'action_name_2': action 2}
action_names = [
    {'action': 'echo', 'controller': get_echo},
]
