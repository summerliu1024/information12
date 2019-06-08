from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # 运行当前Flask应用程序
    app.run(debug=True)
