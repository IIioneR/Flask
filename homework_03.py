from faker import Faker
from flask import Flask
import csv

app = Flask('app')


@app.route("/file")
def show_file():
    list = []
    with open("requirements.txt", "r") as file:
        data = str(file.readlines()).replace("\\n", "<br>")
        list.append(data)

        return str(list).replace(",", "")


@app.route("/csv")
def checker_csv():
    with open("hw.csv", 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        csv_iter = csv_reader
        next(csv_iter)
        total1 = 0
        total2 = 0
        line_count = 0
        for line in csv_reader:
            if line:
                line_count += 1
                total1 += float(line[1])
                total2 += float(line[2])

    return str("Avarage weigth: {}, Avarage growth: {}".format(total1 / line_count, total2 / line_count))


@app.route("/users")
def fake_users():
    fake_data = Faker()
    list = []
    for i in range(1, 101):
        name = fake_data.name()
        email = fake_data.safe_email()
        list.append("user: " + str(i) + " name: " + name + " email: " + email + "<br>")
    return str(list).replace(",", "")


app.run()
