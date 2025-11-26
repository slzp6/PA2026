"""c10_2.py"""

import secrets
import string


def passwd_str():
    """password strings"""
    alpha = string.ascii_letters + string.digits
    passwd = ''.join(secrets.choice(alpha) for i in range(0, 10))
    return passwd


for i in range(5):
    print(f"{i}:  {passwd_str()}")
