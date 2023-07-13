from flask import Blueprint
from typing import Dict, List
from pydantic import BaseModel

from database.questionservice import get_questions_db, check_user_answer_db
from database.startservice import get_user_positions

test_bp = Blueprint('test_process', __name__)


# валидатор вопросов
class Qusetions(BaseModel):
    timer: int
    questions: List[Dict]


# Запрос на получение всех вопросов

@test_bp.route('/get-questions/<string:level>', methods=['GET'])
def get_user_questions(level: str) -> Qusetions.json:
    # Обращение к базе вопросов
    questions = get_questions_db(level)
    print(questions)
    if questions:
        result = []
        timer = 0
        # Пройдемся по каждому вопросу
        for question in questions:
            generate_question = {"question_text": question.main_question,
                                 "variants": [question.answer_1,
                                              question.answer_2,
                                              question.answer_3,
                                              question.answer_4]}
            result.append({'question_id': question.id, 'question': generate_question})
            timer = question.timer

        return Qusetions(**{'timer': timer, 'questions': result}).json()

    return Qusetions(timer=0, questions=[]).json()


# Запрос на проверку ответа от пользователя


@test_bp.route('/check-answer/<int:question_id>/<int:user_answer>', methods=['POST'])
def check_current_user_answer(question_id: int, user_answer: str) -> Dict[str, int]:
    result = check_user_answer_db(question_id, user_answer)

    return {'status': 1 if result else 0}

    # Запрос на вывод результата


@test_bp.route('/done/<int:user_id>/<int:correct_answers>/<string:level>', methods=['POST'])
def user_done_test(user_id: int, correct_answers: int, level: str) -> Dict[str, int]:
    user_position = get_user_positions(user_id, correct_answers, level)

    return {'status': 1, 'correct_answers': correct_answers, 'position_on_top': user_position}
