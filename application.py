from flask import Flask, render_template, request, redirect
import os
import csv
#configure app
app = Flask(__name__)

#Registered Students
students=[]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registered")
def registrered():
    with open("registered.csv", "r") as file:
        reader= csv.reader(file)
        students = list(reader)
    return render_template("registered.html", students=students)

@app.route("/register", methods=["POST"])
def register():
    #TODO
    file = open("registered.csv", "a")
    writer = csv.writer(file)
    writer.writerow((request.form.get("name"),request.form.get("dorm")))
    file.close()
    return redirect("/registered")


if __name__ == "__main__":
    app.run()

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '/templates')
app = Flask(__name__, template_folder=template_path)