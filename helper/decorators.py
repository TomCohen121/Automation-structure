def handle_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            raise Exception(f"❌ General error in {func.__name__}: {e}")
    return wrapper