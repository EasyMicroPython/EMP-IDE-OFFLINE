from flask import Flask
from flask import render_template
from flask import url_for
import threading
import sys
import os
import webbrowser
import time
import fire

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


def wsb(device, port):
    time.sleep(1)
    print('==> Launch browser...')
    webbrowser.open('http://localhost:%s' % port)
    print('==> Enable empwsb...')
    os.system('sudo empwsb %s' % device)


def runserver(device='/dev/ttyUSB0', port=5000):
    thread = threading.Thread(target=wsb, args=(device, port))
    thread.start()
    print('==> Runing server...')
    app.run(port=port)


def main():
    fire.Fire(runserver)


if __name__ == '__main__':
    main()
