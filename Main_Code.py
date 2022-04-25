from flask import Flask, render_template, request, session, redirect, url_for
import pandas as pd

app = Flask(__name__, template_folder="Templates")


@app.route('/landing_page') #route define various endpoints
@app.route('/') #route define various endpoints
def landing():
        return render_template("landing_page.html", title="Landing Page")
        



if __name__ == '__main__':
    app.debug = True
    app.run()


