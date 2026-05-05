from flask import Flask, make_response

# Flask(__name__) 创建应用对象，__name__ 用于定位模板、静态文件等资源。
app = Flask(__name__)

@app.route('/')
def hello():
    # make_response 可以显式创建响应对象，方便设置响应头、Cookie、状态码等。
    response = make_response('Hello World!')

    # 自定义响应头常用于调试、跨域、安全策略等场景。
    response.headers["test_header"] = "cjh"
    return response

if __name__ == '__main__':
    # url_map 可以打印当前应用注册了哪些路由，学习路由时很有用。
    print(app.url_map)

    # debug=True 只适合本地开发，生产环境不要打开。
    app.run(debug=True)
