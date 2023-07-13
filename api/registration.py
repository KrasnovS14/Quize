from flask import Blueprint
from typing import Dict, List
from database.userservice import register_user_db

registration_bp = Blueprint('registation', __name__)


# Запрос на регистрацию

@registration_bp.route('/register/<string:name>/<string:number>', methods=['POST'])
def register_user(name:str, number: str) -> Dict[str, str]:
    user_id = register_user_db(name, number)
    return {'status': 1, 'user_id': user_id}


