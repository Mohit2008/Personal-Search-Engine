from flask import Flask, request, render_template
import sys  # NOQA
import os

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), os.pardir, os.pardir))

from searchEngine.searcher.search import do_search


app = Flask(__name__, template_folder='templates')

@app.route('/')
def display():
    return render_template('index.html')

@app.route('/search/<string:keyword>/', methods=['GET'])
def search(keyword):
    return do_search(keyword)

def runServer():
    app.run()
