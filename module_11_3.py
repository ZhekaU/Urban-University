from pprint import pprint
def introspection_info(*obj):
    info = {
        'type': type(obj),
        'attributes': [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')],
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getattr(obj, '__module__', 'No module attribute'),
        'doc': getattr(obj, '__doc__', 'No docstring')
    }
    return info

number_info = introspection_info(42,'time')
pprint(number_info)
