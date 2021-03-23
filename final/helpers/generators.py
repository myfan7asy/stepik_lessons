"""
A specific file to contain all helper functions (mostly for data generation) which are not directly related to tests.
"""

from datetime import datetime
import string
import random


def generate_unique_email():
    """
    A helper function, which generates a random unique email address, which is required for successful registration.
    :return: str object (uniquely generated username + static domain)
    """
    letters = string.ascii_letters.lower()
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")
    username = random.choice(letters) + current_time
    domain = "@test.gg"
    return username + domain
