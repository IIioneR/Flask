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
    digits = request.args.get('dig', DEFAULT_DIG)
    if str(length).isnumeric() and str(digits).isnumeric():
        if 8 <= int(length) <= 24 and 0 <= int(digits) <= 1:
            gen_symbols = string.ascii_letters + string.digits if digits else string.ascii_letters
            return ''.join([
                random.choice(gen_symbols) for _ in range(int(length))
            ])
    return "wrong lenght or format lenght, or wrong digits"


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
    query = f'select count(DISTINCT FirstName) from customers'
    records = execute_query(query)
    result = '<br>'.join([str(record) for record in records])
    return f"Count distinct users = {str(result).replace(',', '')}"


@app.route("/get-inv-items")
def get_invoice_items():
    query = f'select UnitPrice, Quantity from invoice_items'
    records = execute_query(query)
    total = 0
    for line in records:
        total += (line[0] * line[1])
    return str(f"Total invoice: {int(total*100)/100}")


app.run()
