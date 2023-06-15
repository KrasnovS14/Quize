from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from api import leaders, registration, test_process

app = Flask(__name__)
db= SQLAlchemy()
# Задать конфигурацию для базы данных
app.config['SQLALCHEMT_DATABASE_URI'] = 'sqlite:////quiz.db'

# создание приложения
db.init_app(app)




# Регистрация

app.register_blueprint(leaders.leaders_bp)
app.register_blueprint(registration.registration_bp)
app.register_blueprint(test_process.test_bp)
