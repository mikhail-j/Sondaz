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
import random
print "Content-type: text/html\n"

form = cgi.FieldStorage()
user = form.getvalue("un")
p = form.getvalue("pass")

def current(fn):
    f = open(fn,"r")
    b = f.read()
    f.close()
    b = b.strip("\n")
    if (b.find("\n") != -1):
        b = b.split("\n")
        i = 0
        ln = len(b)
        while (i < ln):
            b[i] = b[i].split(":")
            i += 1
    else:
        b = [b.split(":")]
    return b

def registerd(u):#check for entries
    k = 0
    ln = len(b0)
    while (k < ln):
        if (b0[k][0] == u):
            return True
        else:
            k += 1
    return False

def pswd(u):
    k = 0
    ln = len(b0)
    while (k < ln):
        if (b0[k][0] == u):
            return b0[k][1]
        k += 1
    return None

def keygen():
    fchr_set = "0123456789abcdefghijklmnopqrstuvwxyz"
    string = ""
    i = 0
    while (i < 64):
        string += fchr_set[int(random.random() * 16)]
        i += 1
    return string

def ck(u):
    k = 0
    ln = len(b1)
    while (k < ln):
        if (b1[k][0] == u):
            return True
        k += 1
    return False

def updatekey(key):
    b1 = current("./jwenfis/ijxckgmw.txt")
    k = 0
    ln = len(b1)
    while (k < ln):
        if (b1[k][0] == user):
            b1[k][1] = key
            k = ln
        k += 1
    k = 0
    while (k < ln):
        b1[k] = ":".join(b1[k])
        k += 1
    b1 = "\n".join(b1) + "\n"
    f = open("./jwenfis/ijxckgmw.txt","w")
    f.write(b1)
    f.close()
    return

def newkey(key):
    f = open("./jwenfis/ijxckgmw.txt","a")
    f.write(user + ":" + key + "\n")
    f.close()
    return

def htmlcheck(u):#check for illegal characters
	illegal = "<>:"
	i = 0
	ln = len(illegal)
	while (i < ln):
		if (u.find(illegal[i]) != -1):
			return True
		else:
			i += 1
	return False

b0 = current("./jwenfis/registered-voters.txt")
b1 = current("./jwenfis/ijxckgmw.txt")
print '<html><head><title>My Account....</title><style>a:hover {color: #FF0000;} a {text-decoration: none; color:#000000;}</style><link href="http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,100italic,300italic,400italic,700italic,900italic" rel="stylesheet" type="text/css"><link href="./css/styles0.css" rel="stylesheet" type="text/css"></head><body>'

if (user == None or p == None):
	print '<br><div id="message"><p id="cc">Please check if you submitted your username or password.</p></div></body><script>function load(){ window.location="./register.html"} setTimeout(load, 2500)</script></html>'
elif (htmlcheck(user)):
	print '<br><div id="message"><p id="cc">Please check your username for illegal characters.</p></div></body><script>function load(){ window.location="./register.html"} setTimeout(load, 2500)</script></html>'
elif (not registerd(user)):
    print '<br><div id="message"><p id="cc">Username ' + user + ' does not exist! Please register first!</p></div></body><script>function load(){ window.location="./register.html"} setTimeout(load, 2500)</script></html>'
elif (pswd(user) != p):
    print '<br><div id="message"><p id="cc">The password is incorrect, check if Caps Lock is on.</p></div></body><script>function load(){ window.location="./register.html"} setTimeout(load, 2500)</script></html>'
else:
    cid = keygen()
    if (ck(user)):
        updatekey(cid)
    else:
        newkey(cid)
    print '<div id="ap" style="height:auto; margin: 30px auto; margin-bottom: 0;"><div id="tc"><p id="cc" style="font-size:xx-large; margin:0;">Welcome ' + user + '!</p><br><div style="display: inline-block; text-align:center; margin: auto 0; width:50%;"><a href="./quiz0.py?user=' + user + '&active=' + cid + '"><img src="./images/survey.png"><br>Survey</a></div><div style="display: inline-block; text-align:center; margin: auto 0; width: 50%;"><a href="./cresults.py?user=' + user + '&active=' + cid + '"><img src="./images/chart.png"><br>Survey Results</a></div><br><br></div></div><div id="cr">&copy; Copyright &copy; 2013 Qijia (Michael) Jin .</div></body></html>'
