from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(__name__, static_url_path='/static')


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/resume")
def resume():
    return "<p>comming soon...</p>"
