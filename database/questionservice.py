from database.models import Question, db
import random

# Получить вопросы
def get_questions_db(level):
    # Если уровень не указан

    if level == 'all':
        questions = []
        # Получаем все вопросы с базы
        all_questions = Question.query.all()

        # Рандомные вопросы
        for i in range(20):
            questions.append(random.choice(all_questions))

        return questions


    # если указал сложность, то фильтр по вопросам
    questions_from_level = Question.query.filter_by(level=level).all()
    questions = [random.choice(questions_from_level) for i in range(20)]

    return questions


# Проверка ответа пользователя
def check_user_answer_db(question_id, user_answer):
    current_question= Question.query.get(question_id)

    # Проверка ответа пользователя с реальным ответом в базе

    if current_question.correct_answer == user_answer:
        return True

    return False

# Добавление вопросов в базу (ДЗ)
def add_question_db(main_question, answer_1, answer_2, answer_3, answer_4, correct_answer, level):
    question = Question(main_question=main_question,
        answer_1=answer_1,
        answer_2=answer_2,
        answer_3=answer_3,
        answer_4=answer_4,
        level=level,
        correct_answer=correct_answer)
    db.session.add(question)
    db.session.commit()