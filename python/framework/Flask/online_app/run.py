from app import create_app

# 通过应用工厂创建 Flask app，后续测试或不同环境可以复用 create_app。
app = create_app()

if __name__ == '__main__':
    # 打印路由表，方便学习时确认 URL 和视图函数是否注册成功。
    print(app.url_map)

    # debug=True 只用于本地开发，生产环境应该交给 gunicorn、uwsgi 等服务器运行。
    app.run(debug=True)
