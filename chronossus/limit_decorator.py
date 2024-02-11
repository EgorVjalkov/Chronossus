def limit_decorator(valid_values, if_limit):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if result not in valid_values:
                return if_limit
            else:
                return result

        return wrapper

    return decorator


