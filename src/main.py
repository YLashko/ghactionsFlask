from flask import Flask, Response, render_template
import os
from random import randint

app = Flask(__name__)

@app.route("/<name>", methods=["GET"])
def get_name(name):
    return f"Hello {name}"

@app.route("/", methods=["GET"])
def main():
    number = " ".join([str(randint(0, 10)) for _ in range(200)])
    return render_template("main.html.jinja", number=number, mode=os.environ.get("MODE"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
