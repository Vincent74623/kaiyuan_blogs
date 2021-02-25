from flask import render_template,url_for,redirect
from app_blogs.sign_in import bp
from app_blogs.sign_in.forms import LoginForm
from flask_login import current_user,login_user
from app_blogs.models import User

@bp.route('/sign_ins',methods=['GET','POST'])
def sign_ins():
    if current_user.is_authenticated:
        return redirect(url_for('home_pages.home_page'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('sign_in.sign_ins'))
        login_user(user)
        return redirect(url_for('home_page.home_pages'))
    return render_template('sign_in/sign_ins.html',form=form)