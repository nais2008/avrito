from flask import Flask

app = Flask(__name__)

""" Команды alembic
alembic init alembic -- инициализация
alembic revision --autogenerate -m "Коментарии"
alembic upgrade head - upgrade  --выполняет код для изменения состояния базы
                       downgrade -- код для возврата к предыдущему состоянию
"""


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
