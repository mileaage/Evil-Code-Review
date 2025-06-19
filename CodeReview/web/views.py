from flask import Blueprint, render_template, request
from ..models import review


bp = Blueprint('main', __name__)
reviewer = review.Reviewer()

@bp.route('/')
def home():
    return render_template('index.html')

@bp.route('/review', methods=['POST'])
def review_page():
    code = request.form.get('code', '')
    insult_level = request.form.get('insult_level', 5)
    print(insult_level)
    print('getting response')

    response = reviewer.review_code(code, int(insult_level))
    
    return render_template('review.html', code=code, response=response)