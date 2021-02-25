from app_blogs.home_page import bp
from app_blogs.models import Post
from flask import render_template,request,url_for
from app_blogs import main_app

@bp.route('/')
@bp.route('/index')
def home_pages():
    app = main_app()
    page = request.args.get('page', 1, type=int)

    posts = Post.query.order_by(Post.timeramp.desc()).paginate(page, app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('home_page.home_pages', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('home_page.home_pages', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('home_page/home_pages.html',posts=posts.items,
                           next_url=next_url, prev_url=prev_url)

# timeramp