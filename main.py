 # create a python file called main.py and add the following code to it.

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

pp.route('/')
def index():
    return render_template('index.html')
