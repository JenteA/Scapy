from __future__ import print_function
import subprocess
import os
import sys
from ping import ping
from tcp import tcpping
from arp import arp
from flask import Flask
from flask import request
from flask import render_template, redirect, url_for

processText = ''
ip = ''

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/Scriptje', methods=['POST'])
def my_form_post():
    processText = ''
    ip = request.form['ip']
    port = request.form['port']
    choice = request.form['request']
    delay = request.form['delay']
    nr = request.form['nr']
    print(ip)
    if delay == '':
       delay = 1
    else:
       delay = int(delay)
    if nr == '':
       nr = 1
    else:
       nr = int(nr)
    subprocess.call("echo `pwd`>>succes", shell=True)
    if choice == 'ping':
       processText = ping(ip, delay, nr)
    if choice == 'tcp':
	   processText = tcpping(ip, port, delay, nr)
    if choice == 'arp':
       processText = arp(ip, delay, nr)
       if port != '':
	       port = int(port)
	       processText = tcpping(ip, port)
    if choice == 'arp':
       processText = arp(ip)
    else:
        print('nothing to do')
    return render_template("index.html", processText=processText)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
