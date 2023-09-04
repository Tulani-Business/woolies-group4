from flask import *


app = Flask(__name__)
# app.config['SECRET_KEY'] = ''


@app.route('/')
def index():
    return "hello world"


@app.route('/radio_demo', methods=['POST'])
def radio_demo():
    user = request.form['type']
    return user


if __name__ == "__main__":
    app.run(debug=True)
