from flask import Blueprint
from typing import Dict, List

registration_bp = Blueprint('registation', __name__)


# Запрос на регистрацию

@registration_bp.route('/register/<string:name>/<int:number>', methods=['POST'])
def register_user(name:str, number: int) -> Dict[str, int]:
    pass

