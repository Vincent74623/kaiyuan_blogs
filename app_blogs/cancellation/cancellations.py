from app_blogs.cancellation import bp
from flask_login import logout_user
from flask import url_for,redirect
@bp.route('/cancellations')
def cancellations():
    logout_user()
    return redirect(url_for('home_page.home_pages'))