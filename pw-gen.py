#!/usr/bin/python3
import sys
import random
import string

default_len = 8
def get_random_string(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))

a = default_len
try:
    a = sys.argv[1]

except IndexError as e:
    a = str(default_len)


a = int(a) if a.isdigit() else default_len

print(get_random_string(a))