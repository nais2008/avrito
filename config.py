from flask import Flask
from flask_login import LoginManager
from flask_restful import Api
import datetime as dt

""" Команды alembic
alembic init alembic                                -- инициализация
alembic revision --autogenerate -m "Коментарии"     -- генерация версии изменений
alembic upgrade head                                -- выполняет код для изменения состояния базы
        downgrade                                   -- код для возврата к предыдущему состоянию
"""

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
app.config['PERMANENT_SESSION_LIFETIME'] = dt.timedelta(
    days=15
)

login_manager = LoginManager()
login_manager.init_app(app)

app = Flask(__name__)
api = Api(app)