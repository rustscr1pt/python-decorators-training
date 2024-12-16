import time


def timer_decorator(function):
    def wrapper():
        start = time.time()
        result = function()
        end = time.time()
        print(f"Function {function.__name__} executed in {end - start:.4f} seconds")
        return result
    return wrapper

@timer_decorator
def slow_function():
    import time
    time.sleep(2)
    return "Done"


print(slow_function())