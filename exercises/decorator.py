def demo_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"args:   {args}")
        print(f"kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@demo_decorator
def beispiel(a, b, c=10):
    return a + b + c

beispiel(a=1, b=2, c=3)