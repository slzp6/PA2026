"""q10_2.py"""


def to_upper_camel_case(snake_string):
    """upper camel case"""
    return snake_string.title().replace("_", "")


SNAKE_STR = "user_account"
print(SNAKE_STR)
print(to_upper_camel_case(SNAKE_STR))

print("---")
SNAKE_STR = "user_account_id"
print(SNAKE_STR)
print(to_upper_camel_case(SNAKE_STR))
