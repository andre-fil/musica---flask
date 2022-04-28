from flask import Flask, url_for, render_template
from flask import request, send_file
import glob
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/sounds")
def	sounds():
			music	=	request.args["music"]
			return	send_file(music,	mimetype="audio/mp3")


if (__name__=='__main__'):
    app.run(debug=True)
