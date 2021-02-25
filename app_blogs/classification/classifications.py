from flask import render_template
from app_blogs.classification import bp
from app_blogs.models import Fen

@bp.route('/classifications')
def classifications():
    fens = Fen.query.all()
    return render_template('classification/classifications.html',fens=fens)