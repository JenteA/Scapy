from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    ip = request.form['ip']
    select = request.form.get('request')
    processed_text = text.upper()
    return processed_text

if __name__ == '__main__':
    app.run()