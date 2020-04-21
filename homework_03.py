from faker import Faker
from flask import Flask
import csv

app = Flask('app')


@app.route("/file")
def show_file():
    with open("requirements.txt", "r") as file:
        data = str(file.readlines()).replace("\\n", "<br>")

        return data


@app.route("/csv")
def checker_csv():
    with open("hw.csv", 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        total1 = 0
        total2 = 0
        line_count = 0
        for line in csv_reader:
            print(line)
            if line:
                line_count += 1
                total1 += float(line[' \"Height(Inches)\"'])
                total2 += float(line[' \"Weight(Pounds)\"'])
        result1 = str((total1 / line_count) * 2.54 )
        result2 = str((total2 / line_count) * 0.45359237)
    return "Avarage Height (sm): {}, Avarage Weitght (kg): {} ".format(result1, result2)


@app.route("/users")
def fake_users():
    fake_data = Faker()
    list = []
    for i in range(1, 101):
        name = fake_data.name()
        email = fake_data.safe_email()
        list.append(("user: " + str(i)) + (" name: " + name) + (" email: " + email) + "<br>")
    x = " ".join(list)

    return str(x)


app.run()
