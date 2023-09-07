import re
from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
app.secret_key = 'thisisasecret'
db = SQLAlchemy(app)


def Email_Valid(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # content = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    lname = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    IDnumber = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # task_content = request.form['content']
        name = request.form['stdFName']
        lname = request.form['stdLName']
        email = request.form['stdEmailP']
        address = request.form['stdAddrs']
        IDnumber = request.form['stdId']
        status = request.form['stdStatus']

        email_exist = Todo.query.filter_by(email=email).first()

        if Email_Valid(email):
            if email_exist:
                flash("Student with this email already added", 'error')
            else:
                # model creation
                new_task = Todo(lname=lname, name=name, email=email,
                                IDnumber=IDnumber, status=status, address=address)
            # try:
                db.session.add(new_task)
                db.session.commit()
                flash("Student is added", 'success')
            return redirect('/')
            # except:
            #     return 'there was an issue adding your task'
        else:
            flash("Invalid email address format. Please enter a valid email.", 'error')

    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
