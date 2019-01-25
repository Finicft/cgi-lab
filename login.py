#!/usr/bin/env python3
import os
import cgi
import cgitb
cgitb.enable()
from templates import login_page, secret_page, after_login_incorrect
from secret import username, password

form = cgi.FieldStorage()
f_useranme = form.getfirst("username")
f_password = form.getfirst("password")

request_type = os.environ.get("REQUEST_METHOD","GET")
cookie_string = os.environ.get("HTTP_COOKIE")

c_username = None 
c_password = None 
cookie_kvs = cookie_string.split("; ")
if cookie_kvs:
    for cookie_kv in cookie_kvs:
#render the login form 
        if cookie_kv:
            k,v = cookie_kv.split("=")
            if k == "username":
                c_username = v
            if k == "password":
                c_password = v

if c_username and c_password:
    print()
    print(secret_page(c_username,c_password))

print("Content-Type: text/html")

if request_type == "POST":
    if f_useranme == username and f_password == password:
        #login ok, set cookie 
        print("Set-Cookie: username = {}".format(f_useranme))
        print("Set-Cookie: password = {}".format(f_password))
        print()
        print(secret_page(f_useranme,f_password))
    else:
        print()
        print(after_login_incorrect())
else:
    print()
    print(login_page())
    
