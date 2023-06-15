from main import db
from datetime import datetime


# Таблицы пользователей
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    phone_number= db.Column(db.String, unique=True)
    reg_date = db.Column(db.DateTime, dufault= datetime.now())




# Таблица вопросов
class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    level = db.Column(db.String, dufault='Easy')
    main_questions = db.Column(db.String, nullable=False)
    answer_1 = db.Column(db.String,)
    answer_2 = db.Column(db.String,)
    answer_3 = db.Column(db.String, nullable=True)
    answer_4 = db.Column(db.String, nullable=True)
    correct_answer = db.Column(db.Integer, nullable=False)
    timer = db.Column(db.Integer)



# Таблица лидеров/ результаты
class Result(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))
    questions_id = db.Column((db.Integer, db.ForeingKey('questions.id')))
    user_answer = db.Column(db.String, nullable=False)
    correctness = db.Column(db.Boolean, default=True)
    level = db.Column(db.String)

    user_fk = db.relationship(User)
    questions_fr = db.relationship(Question)
# Таблица для рейтинга
class Rating(db.Model):
    __tablename__ = 'results'
    user_id = db.Column(db.Integer, db.ForeingKey('users.id'))
    user_correct_answer = db.Column(db.Integer, default=0)

    user_fk = db.relationship(User)