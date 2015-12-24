from __future__ import print_function
import subprocess
import os
import sys
from ping import ping
from tcp import tcpping 
from flask import Flask
from flask import request
from flask import render_template, redirect, url_for

ip ='192.168.0.1'

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/Scriptje', methods=['POST'])
def my_form_post():
    ip = request.form['ip']
    print(ip)
    subprocess.call("echo `pwd`>>succes", shell=True)
    processText = ping(ip)
    return render_template("index.html", processText=processText)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
