# myblog

## 一、简介
这是一个使用 Flask 开发的个人博客，其目前运行的地址为：


* http://112.74.173.234/
* http://www.redhongc.top/
* http://redhongc.top/

开源代码地址

* https://github.com/redtecher/myblog

## 二、特点
简单的一个博客系统，功能实现上实现了以下几个功能：
* 发表文章，并能够修改
* 添加了评论的功能
* 实现注册登录，每个用户都能发表文章
* 留言板功能
* 编辑器使用开源的[editor.md](https://github.com/pandao/editor.md)
* markdown解析并展示

## 三、基本架构
### 后端
Flask1.0.2
### 前端
Bootstrap3.3.7+editor.md
### 服务器架设
uwsgi+supervisor+nginx

## 四、截图
![](http://112.74.173.234/image/20180721193854.png)
![](http://112.74.173.234/image/20180721193908.png)

## 五、运行
```
$ virtualenv VENV
(VENV)$ pip install -r requirements.txt
(VENV)$ python manage.py db init
(VENV)$ python manage.py db migrate
(VENV)$ python manage.py db upgrade
(VENV)$ python manage.py runserver
```

## 六、依赖
```
alembic==1.0.0
asn1crypto==0.24.0
astroid==1.6.5
bcrypt==3.1.4
bleach==2.1.3
blinker==1.4
cffi==1.11.5
click==6.7
colorama==0.3.9
cryptography==2.2.2
dominate==2.3.1
Flask==1.0.2
Flask-Admin==1.5.1
Flask-Bcrypt==0.7.1
Flask-Bootstrap==3.3.7.1
Flask-Login==0.4.1
Flask-Mail==0.9.1
Flask-Markdown==0.3
Flask-Migrate==2.2.1
Flask-Moment==0.6.0
Flask-PageDown==0.2.2
Flask-Script==2.0.6
Flask-SQLAlchemy==2.3.2
Flask-WTF==0.14.2
html5lib==1.0.1
idna==2.7
isort==4.3.4
itsdangerous==0.24
Jinja2==2.10
lazy-object-proxy==1.3.1
Mako==1.0.7
Markdown==2.6.11
markdown2==2.3.5
MarkupSafe==1.0
mccabe==0.6.1
pycparser==2.18
pylint==1.9.2
PyMySQL==0.9.2
python-dateutil==2.7.3
python-editor==1.0.3
six==1.11.0
SQLAlchemy==1.2.10
visitor==0.1.3
webencodings==0.5.1
Werkzeug==0.14.1
wrapt==1.10.11
WTForms==2.2.1