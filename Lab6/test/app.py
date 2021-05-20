from flask import Flask
from flask import request, redirect, url_for
import db
USERS = []

# do: FLASK_ENV=development
app = Flask(__name__)

@app.route("/")
def hello_world():
    users = [ f"<p>{u}</p>" for u in USERS]

    return "<p>Aloha, Jamnik!</p>" + "\n".join(users)

@app.route("/add/", methods = ["POST", "GET"])
def add():
    # print(request.form, flush=True)
    if request.method == "GET":
        users = [ f"<p>{u}</p>" for u in USERS]
        return """
        <form method="POST">
            <input name="username"/>
            <button type="submit">Zapisz</button>
        </form>
        """ + "\n".join(users)

    if request.method == "POST":
        db.add_user(request.form.get("username"))
        USERS.append(request.form.get("username"))
        # print(form_data)
        # return render_template("data.html",form_data = form_data)
        return redirect(url_for("add"))
