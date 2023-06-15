from flask import Blueprint
from typing import Dict, List

leaders_bp = Blueprint('leaders', __name__)


# Запрос на получение top 5 участников

@leaders_bp.route('/leaders/<string:level>', methods=['GET'])
def get_top_5_leaders(level: str = 'all') -> Dict[str, List[Dict[str, int]]]:
    pass