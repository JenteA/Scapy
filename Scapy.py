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
    ip = request.form['port']
    choice = request.form['request']
    print(ip)
    subprocess.call("echo `pwd`>>succes", shell=True)
    if choice == 'ping':
       processText = ping(ip)
    if choice == 'tcp':
	processText = tcpping(ip, port)
    if choice == 'arp'
       processText = arp(ip)
    else:
        print('nothing to do')
    return render_template("index.html", processText=processText)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
