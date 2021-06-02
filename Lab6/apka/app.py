from flask import Flask
from flask import request, redirect, url_for

import database_manager as dm
# from database_manager import add_user

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Aloha, Studenci!"


@app.route("/add/", methods = ["POST", "GET"])
def add():
    # print(request.form, flush=True)
    if request.method == "GET":
        return """
        <form method="POST">
            <input name="username"/>
            <button type="submit">Zapisz</button>
        </form>
        """

    if request.method == "POST":
        dm.add_user(request.form.get("username"))

        # print(form_data)
        # return render_template("data.html",form_data = form_data)
        return redirect(url_for("add"))
