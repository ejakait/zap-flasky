import sys
import time
import telepot
from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return 'hello from zappa'

if __name__ =='__main__':
    app.run()