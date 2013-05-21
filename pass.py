#!/usr/bin/python
'''
Copyright (c) 2013 Qijia (Michael) Jin

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
'''

import cgi

form = cgi.FieldStorage()
user = form.getvalue("un")
p = form.getvalue("pass")
f = open("./jwenfis/registered-voters.txt","r")
b2 = f.read()
b2 = b2.strip("\n")
f.close()
if (b2.find("\n") != -1):
    b2 = b2.split("\n")
    i = 0
    ln = len(b2)
    while (i < ln):
        b2[i] = b2[i].split(":")
        i += 1
else:
    b2 = [b2.split(":")]

def htmlcheck(u):#check for illegal characters
	illegal = "<>:"
	k = 0
	ln = len(illegal)
	while (k < ln):
		if (u.find(illegal[k]) != -1):
			return True
		else:
			k += 1
	return False

def duplicate(u):#check for entries
    k = 0
    ln = len(b2)
    while (k < ln):
        if (b2[k][0] == u):
            return True
        else:
            k += 1
    return False

def newaccount(u,pd):
    f = open("./jwenfis/registered-voters.txt", "a")
    f.write(u + ":" + pd + "\n")
    f.close()

def html_form():#form code
	f = open("register.html","r")
	b0 = f.read()
	f.close()
	b0 = b0.strip("\n")
	b1 = b0.split("\n")
	b0 = "".join(b1)
	b1 = b0.find("<center")
	b2 = len(b0)
	string = ""
	while (b1 < b2):
		string += b0[b1]
		b1 += 1
	return string

b1 = html_form()

print "Content-type: text/html\n"
print "<html><head><title>Register an Account!</title>"
print '<link href="./css/styles0.css" rel="stylesheet" type="text/css">'
print '<link href="http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,100italic,300italic,400italic,700italic,900italic" rel="stylesheet" type="text/css"></head><body><br>'

if (user == None):
    print '<div id="message"><p id="cc">Please submit a username!</p></div><br>' + b1
elif (htmlcheck(user)):
	print '<div id="message"><p id="cc">Submitted username had illegal characters.</p></div><br>' + b1
elif (duplicate(user)):
    print '<div id="message"><p id="cc">Submitted username was invalid, '  + user + " already exists!</p></div><br>" + b1
elif (p == None):
    print '<div id="message"><p id="cc">Please submit a password!</p></div><br>' + b1
elif ((len(p) < 8) or (len(p) > 63)):
    print '<div id="message"><p id="cc">Submitted username is invalid, please submit 8-63 character password!</p></div><br>' + b1
else:
    newaccount(user,p)
    print 'Account has been created!</body><script>function load() { window.location="./";} window.setTimeout(load, 2500);</script></html>'

