# Task 6: Multiple Decorators
#
# Create and stack multiple decorators to modify a function. For example:
#
#     uppercase_decorator (Task 1)
#     logging_decorator (Task 2)
#
# Expected Behavior
#
# @uppercase_decorator
# @logging_decorator
# def greet(name):
#     return f"Hello, {name}"
#
# print(greet("Alice"))
# # Output:
# # Function greet called with arguments: ('Alice',), {}
# # Function greet returned: "HELLO, ALICE"
# # "HELLO, ALICE"

def uppercase_decorator(func):
    def wrapper(text: str) -> str:
        result = func(text)
        return result.upper()
    return wrapper

def logging_decorator(function):
    def wrapper(*args):
        print(f"Function {function.__name__} called with arguments: {args}")
        result = function(*args)
        print(f"Function {function.__name__} returned: {result}")
        print(result)
        return result
    return wrapper


@logging_decorator
@uppercase_decorator
def greet(name : str) -> str:
    return f"Hello, {name}"

greet("Egor")