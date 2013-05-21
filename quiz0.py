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
user = form.getvalue("user")
session = form.getvalue("active")

def current_session():
    f = open("./jwenfis/ijxckgmw.txt","r")
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

def active(entries):
    k = 0
    ln = len(entries)
    while (k < ln):
        if ((entries[k][0] == user) and (entries[k][1] == session)):
            return True
        k += 1
    return False

def k_entry(entries):
    k = 0
    ln = len(entries)
    while (k < ln):
        entries[k] = ":".join(entries[k])
        if (entries[k] == user + ":" + session):
            l = k
            k = ln
        k += 1
    entries.pop(l)
    entries = "\n".join(entries) + "\n"
    f = open("./jwenfis/ijxckgmw.txt","w")
    f.write(entries)
    f.close()
    return

print "Content-type: text/html\n"
error = "<html><head><title>404 Not Found</title></head><body><h1>Not Found</h1><p>The requested URL /~qijia.jin/suve/quiz0.py was not found on this server.</p><hr><address>Apache/2.2.22 (Ubuntu) Server at 149.89.150.100 Port 80</address></body></html>"
b0 = current_session()

if ((user == None) or (session == None)):
	print error
elif (not active(b0)):
    print '<html><head><title>Quiz0</title></head><body>This session seems to be invalid, please login again.</body><script>function load(){window.location="./"} setTimeout(load,3500)</script></html>'
else:
    k_entry(b0)
    print '<html><head><title>Quiz 0</title>'
    print '<link href="http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,100italic,300italic,400italic,700italic,900italic" rel="stylesheet" type="text/css"><link href="./css/styles0.css" rel="stylesheet" type="text/css"></head><body><br>'
    print '<div id="ap" style="height: auto;"><div id="tc"><center><b style="font-size: x-large;">Survey</b></center><form action="____quiz0.py" method="post">'
    print '<br>You have been to an island?<br>'
    print '<input type="radio" name="0" value="yes" id="0y"><label for="0y"> Yes </label><input type="radio" name="0" value="no" id="0n"><label for="0n"> No</label><br>'
    print '<br>You have hugged a stranger?<br>'
    print '<input type="radio" name="1" value="yes" id="1y"><label for="1y"> Yes </label><input type="radio" name="1" value="no" id="1n"><label for="1n"> No</label><br>'
    print '<br>Can you drive a car?<br>'
    print '<input type="radio" name="2" value="yes" id="2y"><label for="2y"> Yes </label><input type="radio" name="2" value="no" id="2n"><label for="2n"> No</label><br>'
    print '<br>You have stolen anything?<br>'
    print '<input type="radio" name="3" value="yes" id="3y"><label for="3y"> Yes </label><input type="radio" name="3" value="no" id="3n"><label for="3n"> No</label><br>'
    print '<br>You have lost a friend?<br>'
    print '<input type="radio" name="4" value="yes" id="4y"><label for="4y"> Yes </label><input type="radio" name="4" value="no" id="4n"><label for="4n"> No</label><br>'
    print '<br>Have you ever gotten carsick?<br>'
    print '<input type="radio" name="5" value="yes" id="5y"><label for="5y"> Yes </label><input type="radio" name="5" value="no" id="5n"><label for="5n"> No</label><br>'
    print '<br>Do you think video games are silly?<br>'
    print '<input type="radio" name="6" value="yes" id="6y"><label for="6y"> Yes </label><input type="radio" name="6" value="no" id="6n"><label for="6n"> No</label><br>'
    print '<br>You have been on a plane?<br>'
    print '<input type="radio" name="7" value="yes" id="7y"><label for="7y"> Yes </label><input type="radio" name="7" value="no" id="7n"><label for="7n"> No</label><br>'
    print '<br>You have seen snakes on a plane?<br>'
    print '<input type="radio" name="8" value="yes" id="8y"><label for="8y"> Yes </label><input type="radio" name="8" value="no" id="8n"><label for="8n"> No</label><br>'
    print '<br>You have own/owned a pet?<br>'
    print '<input type="radio" name="9" value="yes" id="9y"><label for="9y"> Yes </label><input type="radio" name="9" value="no" id="9n"><label for="9n"> No</label><br>'
    print '<br>Do you smoke cigarettes?<br>'
    print '<input type="radio" name="10" value="yes" id="10y"><label for="10y"> Yes </label><input type="radio" name="10" value="no" id="10n"><label for="10n"> No</label><br>'
    print '<br>Grades are more important than sleep?<br>'
    print '<input type="radio" name="11" value="yes" id="11y"><label for="11y"> Yes </label><input type="radio" name="11" value="no" id="11n"><label for="11n"> No</label><br>'
    print '<br>This statement is false?<br>'
    print '<input type="radio" name="12" value="yes" id="12y"><label for="12y"> True </label><input type="radio" name="12" value="no" id="12n"><label for="12n"> False</label><br>'
    print '<br>U MAD?<br>'
    print '<input type="radio" name="13" value="yes" id="13y"><label for="13y"> Yes </label><input type="radio" name="13" value="no" id="13n"><label for="13n"> No</label><br>'
    print '<br>Can you triforce?<br>'
    print '<input type="radio" name="14" value="yes" id="14y"><label for="14y"> Yes </label><input type="radio" name="14" value="no" id="14n"><label for="14n"> No</label><br>'
    print '<br>Please enter your password to confirm your answers.<br>'
    print '<input type="password" name="pass" id="tf" style="width: auto;">'
    print '<input type="hidden" name="un" value="' + user + '">'
    print '<br><input type="submit" value="SUBMIT"></form></div></div><div id="cr">&copy; Copyright &copy; 2013 Qijia (Michael) Jin .</div><br><br></body></html>'