from app_blogs.about import bp
from flask import render_template

@bp.route('/abouts')
def abouts():
    return render_template('about/abouts.html')