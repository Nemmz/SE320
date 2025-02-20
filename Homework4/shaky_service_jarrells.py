"""
Author: Isaac Jarrells
File: shaky_service_jarrells.py
Date: February 24, 2025,
Purpose: To add a delay for function calls to reduce the strain on failed called as in example of
         poor network connectivity. Discord does this when failure to connect happens and increases the time
         inbetween connection attempts.
Sources: None at the time of creation.
Version: 1.0 Initial creation of backoff function which limits the amount of requests for a function call.
Version: 1.1 Adds a delay limit of 2.5 and make the decorator have arguments.
"""

from random import randint
from time import sleep, asctime


def backoffargs(initial_delay, back_off_factor, max_delay) -> callable:
    """Provides backoff with arguments needed for the function"""

    def backoff(func: callable) -> callable:
        """Creates delay variables and the increment factor"""
        delay = 0  # delay variable

        def inner(*args, **kwargs) -> callable:
            """Adds a delay to all function calls if they fail gaining exponential time"""
            nonlocal delay
            time = asctime()
            result = func(*args, **kwargs)  # Calls the function to determine a true or false status
            print(f"{time} will be calling {func.__name__} after {delay} seconds delay.")

            while result is False:
                sleep(delay)  # Sleeps for a delay time
                if delay < max_delay:
                    if delay == 0:  # Checks if delay is 0 to set it equal to initial delay after first fail
                        delay = initial_delay
                    delay *= back_off_factor  # Exponential Increase of delay
                    delay = min(delay, max_delay)  # Prevents it going higher than 2.5 sec
                    return result  # Return result if a failed attempt occurred
                else:
                    return result  # Return result if a failed attempt occurred
            delay = 0  # Resets the delay after a successful attempt
            return result  # Return result if a successful attempt occurred

        return inner

    return backoff


@backoffargs(initial_delay=0.1, back_off_factor=1.5, max_delay=2.5)
def call_shaky_service():
    """If 6 is not return it is False and otherwise is True"""
    return 6 == randint(1, 6)


while True:
    print(call_shaky_service())
