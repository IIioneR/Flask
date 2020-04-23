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


@app.route("/get-cust")
def get_customers():
    DEFAUL_STATE = ""
    DEFAULT_CITY = ""
    state = request.args.get('state', DEFAUL_STATE)
    city = request.args.get('city', DEFAULT_CITY)
    query = f'select FirstName, LastName, State, City from customers where State = "{state}" or City = "{city}"'
    records = execute_query(query)
    result = '<br>'.join([str(record) for record in records])
    return result


def execute_query(query):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query)
    records = cur.fetchall()
    return records

@app.route("/get-cust-count")
def get_customers_count():
    query = f'select FirstName from customers'
    records = execute_query(query)
    result = '<br>'.join([str(record) for record in records])
    count = 0
    result = set(result)
    for line in result:
        count += 1
    return str(count)


app.run()