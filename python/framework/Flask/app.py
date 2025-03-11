from flask import Flask

app = Flask(__name__)
# 这行代码创建了一个 Flask 应用实例。__name__ 是一个特殊的 Python 变量，它在模块被直接运行时是 '__main__'，
# 在被其他模块导入时是模块的名字。传递 __name__ 给 Flask 构造函数允许 Flask 应用找到和加载配置文件。

@app.route('/') # 装饰器，用于告诉 Flask 哪个 URL 应该触发下面的函数
def hello():
    return 'hello'
@app.errorhandler(404)
def error404(e):
    return 'Page not found', 404

if __name__ == '__main__':
    app.run(debug=True)
    # 这行代码调用 Flask 应用实例的 run 方法，启动 Flask 内置的开发服务器。
    # debug=True 参数会启动调试模式，这意味着应用会在代码改变时自动重新加载，并且在发生错误时提供一个调试器。