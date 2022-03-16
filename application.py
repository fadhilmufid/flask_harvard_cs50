from xxlimited import foo
from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def index():
    name = request.args.get("name", "world")
    return render_template("index.html", foo=name)

if __name__ == "__main__":
    app.run()

project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, '/templates')
app = Flask(__name__, template_folder=template_path)