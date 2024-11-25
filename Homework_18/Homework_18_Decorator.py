#1. Logging the function
import logging

logging.basicConfig(
    filename="file_with_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"The result is: {result}")
        logger.info(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

@log_decorator
def raise_to_power(a, b):
    return a ** b

raise_to_power(3, 5)

# 2. Exceptions

def catch_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            divided = func(*args, **kwargs)
            print(f'The divided result is: {divided}')
            return divided
        except Exception as e:
            print(f'The Error is:{e}')
            return print(f'Select the another value for division')
    return wrapper

@catch_exceptions
def divide(a, b):
    return a / b

divide(1, 0)
divide(2, 5)