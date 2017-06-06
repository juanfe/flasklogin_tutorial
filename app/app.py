from flask import Flask

app = Flask(__name__)
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database/database.sqlite'


@app.route('/')
def index():
    return "Welcome to Flask"


if __name__ == '__main__':
    app.run(port=5000, host='localhost')
