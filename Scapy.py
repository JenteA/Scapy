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
    #return redirect(url_for('index.html'))	
    #return render_template(url_for("index.html"))
    return render_template("index.html")

@app.route('/Scriptje', methods=['POST'])
def my_form_post():
    ip = request.form['ip']
    #select = str(request.form.get['request'])
    print(ip)
    subprocess.call("echo `pwd`>>succes", shell=True)
    #subprocess.call("python_netraw ping.py", shell=True)
    ping(ip)
    #os.system("ping.py")
    #background_scripts[id] = True
    #execfile("ping.py")
    return render_template("index.html", ip=ip)
    
@app.route("/Scriptje")
def run_script(id):
    subprocess.call("ping.py", shell=True)
    #os.system("ping.py")
    background_scripts[id] = True
    #execfile("ping.py")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
