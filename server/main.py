from flask import render_template, url_for, redirect, abort, request, jsonify, make_response
from werkzeug.utils import secure_filename
from config import *
import os


# Функция для проверки и сохранения изображения продукта
def save_image_product(image):
    if image:
        filename = secure_filename(image.filename)
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        image.save(image_path)
        return filename
    return None


@app.route('/members', methods=['GET', 'POST'])
def index():
    return jsonify({
        "title": [
            "ch",
            "qwe",
            "asd"
        ]
    })


# страница ошибки 401
@app.errorhandler(401)
def unauthorized(error):
    return render_template(
        '',
        error=error.code,
        message="У вас нет доступа к этой странице, либо вы не авторизованы",
        title="401 Unauthorized",
        css=url_for(
            "static",
            filename="css/error.css")
    ), 401


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5050, debug=True)