"""
Author: Isaac Jarrells
File: shaky_service_jarrells.py
Date: February 24, 2025
Purpose: To add a delay for function calls to reduce the strain on failed called as in example of
         poor network connectivity. Discord does this when failure to connect happens and increases the time
         inbetween connection attempts.
Sources: None at the time of creation.
Version: 1.0
"""

from random import randint
from time import sleep, asctime


def backoff(func: callable) -> callable:
    """Creates delay variables and the increment factor"""
    inital_delay = 0.01
    back_off_factor = 2
    delay = 0

    def inner(*args, **kwargs):
        """Adds a delay to all function calls if they fail gaining exponential time"""
        nonlocal delay
        time = asctime()
        result = func(*args, **kwargs)  # Calls the function to determine a true or false status
        print(f"{time} will be calling {func.__name__} after {delay} seconds delay.")

        while result is False:
            sleep(delay)  # Sleeps for a delay time
            if delay == 0:  # Checks if delay is 0 to set it equal to initial delay after first fail
                delay = inital_delay
            delay *= back_off_factor # Exponential Increase of delay
            return result  # Return result if a failed attempt occurred
        delay = 0  # Resets the delay after a successful attempt
        return result  # Return result if a successful attempt occurred
    return inner

@backoff
def call_shaky_service():
    """If 6 is not return it is False and otherwise is True"""
    return 6 == randint(1, 6)


while True:
    print(call_shaky_service())