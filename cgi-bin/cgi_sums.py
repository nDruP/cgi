#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()

form = cgi.FieldStorage()
try:
    values = form.getlist('val')
    int_values = [int(x) for x in values]
    total = sum(int_values)
    body = "Your total is {}".format(total)
except (ValueError, TypeError):
    body = "Problem values inserted into query"

print(body)
