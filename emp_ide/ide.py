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
    print(
        ' \033[1;31m--> If the browser is not open as expected: ctrl + click the link below\033[0m')
    print(' \033[1;31m--> http://localhost:%s\033[0m' % port)
    print('==> Enable empwsb...')
    os.system('empwsb %s' % device)


def runserver(device='/dev/ttyUSB0', port=5000):
    thread = threading.Thread(target=wsb, args=(device, port))
    thread.start()
    print('==> Runing server...')
    app.run(port=port)


def main():
    fire.Fire(runserver)


if __name__ == '__main__':
    main()
