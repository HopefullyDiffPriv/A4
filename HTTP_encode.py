#!/usr/bin/env python3

user = '-'
def tobeencoded(user):
    result = ''
    for char in user:
        new = hex(ord(char))
        new.strip('0')
        result += '%' + new[2:]
    return result

results = (tobeencoded(user))
print(results)

