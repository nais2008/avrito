from flask import render_template, url_for, redirect, abort, request, jsonify, make_response
from config import *


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()