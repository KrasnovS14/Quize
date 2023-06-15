from database.models import User, db


# Регистрация пользователей

def register_user_db(name, phone_number):
    checker = check_user_db(phone_number)


    if  checker:
        return checker

    # Если нет пользователя, то регистрация
    new_user = User(name=name, phone_number=phone_number)
    db.session.add((new_user))
    db.session.commit()

    return new_user.id



# Проверка пользователя
def check_user_db(phone_number):
    checker = User.query.filter(phone_number=phone_number).first()

    if checker:
        return checker.id

    return False