def demo_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@demo_decorator
def beispiel(a, b, c=10):
    return a + b + c

beispiel(1, 2, c=99)
beispiel(5, 6, 7)
beispiel(a=1, b=2, c=3)