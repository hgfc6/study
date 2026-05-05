# aiohttp 异步 Web 服务示例
#
# 运行方式：
#     python 11_async_io/003_async_http.py
#
# 访问：
#     http://127.0.0.1:8080/
#     http://127.0.0.1:8080/cjh
#
# aiohttp 不是标准库，如果没有安装，本文件会给出安装提示并安全退出。


def create_app():
    """创建 aiohttp Web 应用。"""

    try:
        from aiohttp import web
    except ImportError:
        print("未安装 aiohttp，请先执行：pip install aiohttp")
        return None

    async def index(request):
        """首页路由。"""

        text = "<h1>Index Page</h1>"
        return web.Response(text=text, content_type="text/html")

    async def hello(request):
        """路径参数示例。"""

        name = request.match_info.get("name", "World")
        text = f"<h1>Hello, {name}</h1>"
        return web.Response(text=text, content_type="text/html")

    app = web.Application()

    # aiohttp 使用 web.get、web.post 等函数注册路由。
    app.add_routes(
        [
            web.get("/", index),
            web.get("/{name}", hello),
        ]
    )

    return app


def main() -> None:
    """启动 aiohttp 开发服务器。"""

    try:
        from aiohttp import web
    except ImportError:
        print("未安装 aiohttp，请先执行：pip install aiohttp")
        return

    app = create_app()

    if app is None:
        return

    # run_app 是开发运行方式，生产环境通常会交给 ASGI/WSGI 服务器或容器编排。
    web.run_app(app, host="127.0.0.1", port=8080)


if __name__ == "__main__":
    main()
