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

b2 = []
b3 = []
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
        b2.append(b1[i][2])
    else:
        b1[i][2] = b0[1]
        b2.append(b1[i][2])
    b3.append(b1[i][1])
    i += 1
b1 = None

def inputs(entries, p):
    count = 0
    i = 0
    ln2 = len(entries[p])
    while (i < ln2):
        if (entries[p][i] == "yes"):
            count += 1
        i += 1
    return count

def js(entry):
	i = 0
	ln = len(entry)
	print '<script>'
	while (i < ln):
		b = inputs(entry, i)
		if (i == 12):
			print 'var p' + str(i + 1) + ' = [{ value: 1, color: "#000000"}]; var b' + str(i + 1) +' = new Chart(document.getElementById("canvas' + str(i + 1) + '").getContext("2d")).Pie(p' + str(i + 1) + ',defaults = {segmentShowStroke : false});'
		elif (b == len(entry[i])):
			print 'var p' + str(i + 1) + ' = [{ value: 1, color: "#00497E"}]; var b' + str(i + 1) +' = new Chart(document.getElementById("canvas' + str(i + 1) + '").getContext("2d")).Pie(p' + str(i + 1) + ',defaults = {segmentShowStroke : false});'
		elif (b == 0):
			print 'var p' + str(i + 1) + ' = [{ value: 1, color: "#9E1623"}]; var b' + str(i + 1) +' = new Chart(document.getElementById("canvas' + str(i + 1) + '").getContext("2d")).Pie(p' + str(i + 1) + ',defaults = {segmentShowStroke : false});'
		else:
			print 'var p' + str(i + 1) + ' = [{ value: ' + str(b) + ', color: "#00497E"}, { value: ' + str(len(entry[i]) - b) + ', color: "#9E1623"}]; var b' + str(i + 1) +' = new Chart(document.getElementById("canvas' + str(i + 1) + '").getContext("2d")).Pie(p' + str(i + 1) + ');'
		i += 1
	print '</script><script src="./js/main.js" type="text/javascript"></script>'
	return

def r(entry):
    i = 0
    ln = len(entry)
    while (i < ln):
        if (i == 12):
            print '<a style="text-decoration: none; color: #000000;" href="javascript:s' + str(i) + '();"><div style="margin:0; padding:20px 0; width: 100%; background-color: #DBDBDB;">Question 13 - ' + b3[i] + '</div></a><div id="q' + str(i) + '" style="display: none;"><div id="qr" style="display:block; background-color: #DBDBDB;"><canvas id="canvas13" height="300" width="300"></canvas><div id="cck"><div id="ck" style="left: 20px;"><img src="./images/black.png" style="padding-right:10px;"> True and False</div></div></div><div id="buffering" style="display:none;"><center><img src="./images/load.gif" style="margin: 100px auto;"></center></div></div><br>'
        elif (i % 2 == 0):
            print '<a style="text-decoration: none; color: #000000;" href="javascript:s' + str(i) + '();"><div style="margin:0; padding:20px 0; width: 100%; background-color: #DBDBDB;">Question ' + str(i + 1) + ' - ' + b3[i] + '</div></a><div id="q' + str(i) + '" style="display: none;"><div id="qr" style="display:block; background-color: #DBDBDB;"><canvas id="canvas' + str(i + 1) + '" height="300" width="300"></canvas><div id="cck"><div id="ck"><img src="./images/yes.png" style="padding-right:10px;"> Yes<br><br><img src="./images/no.png" style="padding-right:10px;"> No</div></div></div><div id="buffering" style="display:none;"><center><img src="./images/load.gif" style="margin: 100px auto;"></center></div></div><br>'
        else:
            print '<a style="text-decoration: none; color: #000000;" href="javascript:s' + str(i) + '();"><div style="margin:0; padding:20px 0; width: 100%;">Question ' + str(i + 1) + ' - ' + b3[i] + '</div></a><div id="q' + str(i) + '" style="display: none;"><div id="qr" style="display:block;"><canvas id="canvas' + str(i + 1) + '" height="300" width="300"></canvas><div id="cck"><div id="ck"><img src="./images/yes.png" style="padding-right:10px;"> Yes<br><br><img src="./images/no.png" style="padding-right:10px;"> No</div></div></div><div id="buffering" style="display:none;"><center><img src="./images/load.gif" style="margin: 100px auto;"></center></div></div><br>'
        i += 1
    return

print "Content-type: text/html\n"
b0 = current_session()

if ((user == None) or (session == None)):
	print '<html><head><title>404 Not Found</title><style type="text/css"></style></head><body><h1>Not Found</h1><p>The requested URL /~qijia.jin/suve/cresults.py was not found on this server.</p><hr><address>Apache/2.2.22 (Ubuntu) Server at 149.89.150.100 Port 80</address></body></html>'
elif (not active(b0)):
    print '<html><head><title>Quiz0</title></head><body>This session seems to be invalid, please login again.</body><script>function load(){window.location="./"} setTimeout(load,3500)</script></html>'
else:
    k_entry(b0)
    print '<html><head><title>Survey Results</title><script src="./js/chart.js" type="text/javascript"></script>'
    print '<link href="http://fonts.googleapis.com/css?family=Lato:100,300,400,700,900,100italic,300italic,400italic,700italic,900italic" rel="stylesheet" type="text/css"><link href="./css/styles0.css" rel="stylesheet" type="text/css"></head><body><br>'
    print '<div id="ap" style="margin: 30px auto;height: auto; margin-bottom: 0;"><div id="tc">'
    r(b3)
    js(b2)
    print '</div></div><div id="cr">&copy; Copyright &copy; 2013 Qijia (Michael) Jin .</div><br><br></body></html>'
