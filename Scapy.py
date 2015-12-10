from __future__ import print_function
import sys
from ip.py import ping
from tcp.py import tcpping 
from flask import Flask
from flask import request
from flask import render_template

ip ='192.168.0.1'

app = Flask(__name__)

def run_script(id):
    subprocess.call([select + ".py", ip])
    background_scripts[id] = True

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    ip = request.form('ip')
    select = request.form.get('request')
    
    
@app.route('/generate')
def generate():
    id = str(uuid.uuid4())
    background_scripts[id] = False
    threading.Thread(target=lambda: run_script(id)).start()
    return render_template('processing.html', id=id)



print(ip, file=sys.stderr)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
