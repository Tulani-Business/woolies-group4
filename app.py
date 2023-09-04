from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = ''


@app.route('/')
def index():
    return "hello world"


if __name__ == "_main_":
    app.run(debug=True)
