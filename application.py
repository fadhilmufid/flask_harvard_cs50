from flask import Flask, render_template, request, redirect
import os
#configure app
app = Flask(__name__)

#Registered Students
students=[]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registrants")
def registrants():
    return render_template("registered.html", students=students)

@app.route("/register", methods=["POST"])
def register():
    name = request.form.get("name")
    dorm = request.form.get("dorm")
    if not name or not dorm:
        return render_template("failure.html")
    students.append(f"{name} from {dorm}")
    return redirect("/registrants")
    #TODO


if __name__ == "__main__":
    app.run()

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '/templates')
app = Flask(__name__, template_folder=template_path)