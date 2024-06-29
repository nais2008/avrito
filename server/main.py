from flask import render_template, url_for, redirect, abort, request, jsonify, make_response
from werkzeug.utils import secure_filename
from config import *
import os


@app.route('/api/users', methods=['GET'])
def users():
    return jsonify({
        "users": [
            "efw",
            "wefwef",
            "wefwefwef"
        ]
    })


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5050, debug=True)