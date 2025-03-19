from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response('Hello World!')
    response.headers["test_header"] = "cjh"
    return response

if __name__ == '__main__':
    print(app.url_map)
    app.run(debug=True)