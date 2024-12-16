# Task 3: Execution Time Decorator
#
# Create a decorator called timer_decorator that measures the time it takes for a function to execute.
# Expected Behavior
#
# @timer_decorator
# def slow_function():
#     import time
#     time.sleep(2)
#     return "Done"
#
# print(slow_function())
# # Output:
# # Function slow_function executed in 2.0001 seconds
# # Done

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