
from flask import Flask

app = Flask(__name__)

@app.route('/')
def default():
    return "HOME PAGE"


@app.route('/details')
def details():
    return "Employment Details"


@app.route('/help')
def help():
    return "Help is Here!!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)

