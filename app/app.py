from flask import Flask, request, render_template  # redirect, url_for

from forms import SignupForm
from database import db
from models import User

app = Flask(__name__)


app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/testtutorial.db'


def init_db():
    db.init_app(app)
    db.app = app
    db.create_all()


@app.route('/')
def index():
    return "Welcome to Flask"


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()

    if request.method == 'GET':
        return render_template('signup.html', form=form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            if 'user already exist in database':
                return "Email address already exists"
            else:
                return "Will create user here"
        else:
            return "Form didn't validate"

if __name__ == '__main__':
    init_db()
    app.run(port=5000, host='localhost')
