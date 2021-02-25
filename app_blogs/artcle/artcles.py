from app_blogs.artcle import bp
from flask import render_template,request,redirect,url_for
from app_blogs.artcle.forms import ArtcleForm
from app_blogs.models import Post,Fen
from app_blogs import db
from flask_login import login_required

# 写文章试图函数
@bp.route('/xie_artcles',methods=['GET','POST'])
@login_required
def xie_artcles():
    form = ArtcleForm()
    if form.validate_on_submit():
        if Fen.query.filter_by(name=form.body_fenlei.data).first():
            fe = Fen.query.filter_by(name=form.body_fenlei.data).first()
        else:
            cj = Fen(name=form.body_fenlei.data)
            db.session.add(cj)
            db.session.commit()
            fe = Fen.query.filter_by(name=form.body_fenlei.data).first()
        pos = Post(body_title=request.form['body_title'],
                   body_url=form.body_url.data,
                   body=request.form['body'],
                   fe=fe)
        db.session.add(pos)
        db.session.commit()
        return redirect(url_for('home_page.home_pages'))

    return render_template('artcle/xie_artcles.html',form=form)

# 显示要删除的文章
@bp.route('/xianshi')
@login_required
def xianshi():
    # 获取全部文章，因为要根据文章id来删除文章
    posts = Post.query.order_by(Post.timeramp.desc()).all()

    return render_template('artcle/xianshi.html',posts=posts)


# 删除文章试图函数
@bp.route('/delete_artcles/<int:post_id>')
@login_required
def delete_artcles(post_id):
    p = Post.query.get(post_id)
    db.session.delete(p)
    db.session.commit()
    return redirect(url_for('artcle.xianshi'))

# 打开文章正文函数
@bp.route('/artcles/<int:artcles_id>')
def artcles(artcles_id):
    posts = Post.query.get(artcles_id)
    return render_template('artcle/artcles.html',posts=posts)

