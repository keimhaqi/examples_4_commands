from functools import wraps
from requests import request
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("I am doing some boring work before executing a_func()")

        a_func()

        print("I am doing some boring work after executing a_func()")
    
    return wrapTheFunction


# def a_function_requring_decoration():
#     print("I am the function which needs some decoration to remove my foul smell.")

# a_function_requring_decoration()

# a_function_requring_decoration = a_new_decorator(a_function_requring_decoration)

# a_function_requring_decoration()

@a_new_decorator
def a_function_requring_decoration():
    """Hey you! Decorate me!"""
    print("I am the function which needs some decoration to "
            "remove my foul smell")

# a_function_requring_decoration()

# print(a_function_requring_decoration.__name__)

# def decorator_name(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         if not can_run:
#             return "Function will not run."
#         return f(*args, **kwargs)
#     return decorated

# @decorator_name
# def func():
#     return("Function is running.")

# can_run = True
# print(func())

# can_run = False
# print(func())


# def requires_auth(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         auth = request.authorization
#         if not auth or not check_auth(auth.username, auth.password):
#             authenticate()
#         return f(*args, **kwargs)
#     return decorated

# def logit(func):
#     @wraps(func)
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#     return with_logging

# @logit
# def addition_func(x):
#     """Do some math."""
#     return x + x


# result = addition_func(4)


def logit(logfile = "out.log"):
    def logging_decorator(func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):
            log_string = func.__name__ + " was called."
            print(log_string)
            # open logfile, and write info into it.
            with open(logfile, 'a') as opened_file:
                opened_file.write(log_string + "\n")
            return func(*args, **kwargs)
        return wrapped_function
    return logging_decorator

@logit()
def myfunc1():
    pass

myfunc1()

@logit(logfile='func2.log')
def myfunc2():
    pass

myfunc2()