from flask import Flask
from flask import render_template
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return render_template('index.html')


def runserver():
    manager.run()


if __name__ == '__main__':
    runserver()
