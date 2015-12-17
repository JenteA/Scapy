from __future__ import print_function
import sys
from ping import ping
from tcp import tcpping 
from flask import Flask
from flask import request
from flask import render_template

ip ='192.168.0.1'

app = Flask(__name__)

@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    ip = request.form('ip')
    select = request.form.get('request')
    print(ip);
    
@app.route('/Scriptje')
def run_script(id):
    subprocess.call([select, ip])
    background_scripts[id] = True




print(ip, file=sys.stderr)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
