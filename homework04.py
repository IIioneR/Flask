import json
import os
import random
import string
import sqlite3

import requests
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/gen_pas')
def gen_password():
    DEFAUL_LENGHT = 10
    DEFAULT_DIG = 0
    length = request.args.get('length', DEFAUL_LENGHT)
    digits = int(request.args.get('dig', DEFAULT_DIG))
    if str(length).isnumeric():
        if 8 <= int(length) <= 24:
            if digits == 0:
                return ''.join([
                    random.choice(string.ascii_lowercase)
                    for _ in range(int(length))
                ])
            elif digits == 1 or digits == "":
                return ''.join([
                random.choice(string.hexdigits)
                for _ in range(int(length))
            ])
    return "wrong lenght or format lenght"


app.run()