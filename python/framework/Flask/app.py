from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
# 这行代码创建了一个 Flask 应用实例。__name__ 是一个特殊的 Python 变量，它在模块被直接运行时是 '__main__'，
# 在被其他模块导入时是模块的名字。传递 __name__ 给 Flask 构造函数允许 Flask 应用找到和加载配置文件。
app.secret_key = "cjh"
users = {'admin': 'password'}
@app.route('/') # 装饰器，用于告诉 Flask 哪个 URL 应该触发下面的函数
def home():
    if 'username' in session:
        return f'欢迎回来， {session["username"]}!'
    return '你尚未登录。请登录以查看此内容。'


@app.errorhandler(404)
def error404(e):
    return 'Page not found', 404

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            flash('登录成功！')
            return redirect(url_for('home'))
        else:
            flash('用户名或密码错误，请重试。')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('你已成功登出。')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    # 这行代码调用 Flask 应用实例的 run 方法，启动 Flask 内置的开发服务器。
    # debug=True 参数会启动调试模式，这意味着应用会在代码改变时自动重新加载，并且在发生错误时提供一个调试器。