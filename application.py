#!/usr/bin/env python3

from flask import Flask, render_template, url_for


application = Flask(__name__)


@application.route("/")
def render_static():
    return render_template("index.html")


if __name__ == "__main__":
    application.run(debug=True)
