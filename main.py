from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.models import db

app = Flask(__name__)
# Задать конфигурацию для базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'

# создание приложения
db.init_app(app)

from api import leaders, registration, test_process


# Регистрация

app.register_blueprint(leaders.leaders_bp)
app.register_blueprint(registration.registration_bp)
app.register_blueprint(test_process.test_bp)
