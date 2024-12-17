def introspection_info(*obj):
    info = {
        'type': type(obj),
        'attributes': dir(obj),
        'methods': [method for method in dir(obj) if callable(getattr(obj, method))],
        'module': getattr(obj, '__module__', 'No module attribute'),
        'doc': getattr(obj, '__doc__', 'No docstring')
    }
    return info
number_info = introspection_info(42,"time")
print(number_info)