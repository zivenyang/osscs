import re


def is_valid_param(ch):
    return re.match(r'[0-9a-zA-Z\-_@%]', ch)

