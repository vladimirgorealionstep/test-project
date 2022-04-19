from flask import Flask

app = Flask(__name__)


@app.route('/')
def add_text():
    return 'Love Chickens!'

if __name__ == '__main__':
    app.run()
