# 二次元博客

# 目录结构
```
blogs/
	app_blogs/
		home_page/     首页蓝图
			__init__.py
			home_pages.py
		classification/	分类蓝图
			__init__.py
			classifications.py
		about/		关于蓝图
			__init__.py
			abouts.py
		sign_in/		登录蓝图
			__init.py
			sign_ins.py
		cancellation/	注销蓝图
			__init.py
			cancellations.py
		artcle/		文章蓝图
			__init.py
			artcles.py	       ---->这里有三个试图函数，文章正文，写文章，删除文章
		static/		静态文件
			js/	js文件
			css/	css文件
			images/	图片文件
		templates/	模板文件
			home_page/	首页模板
				home_pages.html
			classification/	分类模板
				classifications.html
			about/		关于模板
				abouts.html
			sign_in/		登录模板
				sign_ins.html
			artcle/		文章模板
				artcles.html	文章正文
				xie_artcles.html	写文章
				delete_artcles.html		删除文章
		base.html
		__init.py		工厂函数
		models.py	数据库模型文件
.env
config.py		配置文件
wsgi.py		主程序
```

# 如何安装库和启动?
解压文件后，请进入文件，这里我使用的是命令行：
```
cd kaiyuan_blogs
```
然后使用python的包管理pip安装所有的第三方库：
```
pip3 install -r requirements.txt
```

这样子我们的所有的库都安装完成了。

有些小伙伴就问，就这，这么简单吗，没有其他操作了吗？

作者：错！你们还没有创建数据库呢。

小伙伴：不会吧。还要安装数据库啊！

作者：错！我们是使用python的数据库。我们不需要格外安装数据库。

小伙伴：这样子，那我就放心了。

小伙伴：我看视频好像只有登录页面，没有注册页面啊？

作者：因为我是面向个人博客，不开放第二人注册，你们需要在后台命令行注册。

小伙伴：这样子。

好啦！你们想问的应该是以上问题吧?如果还有什么疑问。

请到微信公众号：雪影IP工作室

向我提问吧？

好了，开始创建数据库和创建用户,注意我从一开始都没有退出博客项目。

创建数据库，在命令行输入：
```
flask db init
```

创建数据库迁移：
```
flask db migrate -m "one table"
```

提交数据库：
```
flask db upgrade
```

启用flask shell ：
```
flask shell
```

导入模块创建用户：
```
from app_blogs import db
from app_blogs.models import User

u = User(username="你的用户名",email="你的邮箱@qq.com")
u.set_password('你的密码')
db.session.add(u)
db.session.commit()
quit()
```
然后就创建成功了。

启动博客，这里我使用的是个人计算机，如果你们使用的是服务器请百度怎么搭建flask哈！

在命令行：
```
flask run
```

如果你们想在局域网都能访问到你的博客，那就使用以下命令：
```
flask run -h 0.0.0.0 -p 5000
```
局域网访问要你的计算机IP地址，这个你可以百度windows怎么查看ip地址。

代码任意修改，欢迎贡献！
