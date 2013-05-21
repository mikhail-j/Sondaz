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
b0 = [form.getvalue("0")]
b0.append(form.getvalue("1"))
b0.append(form.getvalue("2"))
b0.append(form.getvalue("3"))
b0.append(form.getvalue("4"))
b0.append(form.getvalue("5"))
b0.append(form.getvalue("6"))
b0.append(form.getvalue("7"))
b0.append(form.getvalue("8"))
b0.append(form.getvalue("9"))
b0.append(form.getvalue("10"))
b0.append(form.getvalue("11"))
b0.append(form.getvalue("12"))
b0.append(form.getvalue("13"))
b0.append(form.getvalue("14"))

p = form.getvalue("pass")
user = form.getvalue("un")
login_direct = '<html><head><script>function load(){ window.location="./" } setTimeout(load,4500)</script></head>'

def voted(u):
    f = open("./jwenfis/voters.txt","r")
    b = f.read()
    f.close()
    b = b.strip(",")
    b = b.split(",")
    return u in b

print "Content-type: text/html\n"

if (p == None):
    print '<html><head><script>function load(){window.location="./wp.html";} load();</script></head></html>'
elif (None in b0):
    print '<html><head><script>function load(){window.location="./ma.html";} load();</script></head></html>'
elif (voted(user)):
    f = open("./jwenfis/voters.txt","r")
    b1 = f.read()
    f.close()
    b1 = b1.strip(",")
    b1 = b1.split(",")
    i = 0
    ln = len(b1)
    while (i < ln):
        if (user == b1[i]):
            b2 = i
            i = ln
        i += 1
    b1 = None
    f = open("./jwenfis/votes.txt","r")
    b1 = f.read()
    f.close()
    b1 = b1.strip("\n")
    b1 = b1.split("\n")
    i = 0
    ln = len(b1)
    while (i < ln):
        b1[i] = b1[i].split(":")
        if (b1[i][2] != ""):
            b1[i][2] = b1[i][2].split(",")
            b1[i][2][b2] = b0[i]
            b1[i][2] = ",".join(b1[i][2])
        else:
            b1[i][2] = b0[1]
        b1[i] = ":".join(b1[i])
        i += 1
    b1 = "\n".join(b1) + "\n"
    f = open("./jwenfis/votes.txt","w")
    f.write(b1)
    f.close()
    print '<html><script>function load(){window.location="./thank_you.html";}load();</script></html>'
    
else:
    f = open("./jwenfis/voters.txt","a")
    f.write(user + ",")
    f.close()
    f = open("./jwenfis/votes.txt","r")
    b1 = f.read()
    f.close()
    b1 = b1.strip("\n")
    b1 = b1.split("\n")
    i = 0
    ln = len(b1)
    while (i < ln):
        b1[i] = b1[i].split(":")
        if (b1[i][2] != ""):
            b1[i][2] = b1[i][2].split(",")
            b1[i][2].append(b0[i])
            b1[i][2] = ",".join(b1[i][2])
        else:
            b1[i][2] = b0[i]
        b1[i] = ":".join(b1[i])
        i += 1
    b1 = "\n".join(b1) + "\n"
    f = open("./jwenfis/votes.txt","w")
    f.write(b1)
    f.close()
    print '<html><script>function load(){window.location="./thank_you.html";}load();</script></html>'
    