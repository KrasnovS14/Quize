from database.models import Result, db, Rating


# Получить рейтинг пользователя
def get_rating_db(level):
    # Если по всем направлениям
    user_position = Rating.query.order_by(Rating.user_correct_answer.desc()).filter_by(level=level)

    user_ids = [{i.user_id: i.user_crrect_answers} for i in user_position]

    return user_ids[:5]

# Добавление ответа пользователя
def add_user_answer_db(user_id, user_answer, correctness, level):
    result = Result(user_id=user_id,user_answer=user_answer,correctness=correctness, level=level)
    db.session.add(result)
    db.session.commit()


# Добавление в рейтинг

def add_user_rating_db(user_id, correct_answers, level):
    # проверка есть ли пользователь в таблице(rating)
    user_rating = Rating.query.filter_by(user_id=user_id, level= level).first()
    if user_rating:
        user_rating.user_correct_answer += correct_answers

    else:
        user_rating = Rating(user_id=user_id,
                             user_correct_answer=correct_answers, level = level)
        db.session.add(user_rating)
    db.session.commit()


# Получить позицию пользователя в топе
def get_user_positions(user_id, level, correct_answers):
    register_user_rating = add_user_rating_db(user_id, correct_answers, level)

    user_position = Rating.query.order_by(Rating.user_correct_answer.desc()).filter_by(level=level)
    user_ids = [i.user_id for i in user_position]

    return user_ids.index(user_id) + 1



