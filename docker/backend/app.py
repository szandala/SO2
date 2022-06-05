from flask import Flask, jsonify, make_response, request
from werkzeug.security import generate_password_hash, check_password_hash
import pprint
import datetime
import jwt
from flask_cors import CORS
import mongo_functions

# flask pyjwt flask-cors

def token_required(f):
    def decorator(*args, **kwargs):
        token = None
        pprint.pprint(request.headers)
        if "X-Access-Token" in request.headers:
            token = request.headers["X-Access-Token"]

        if not token:
            return jsonify({"message": "A valid token is missing"})
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = USER_DATA.get(data.get("username"))
        except:
            return jsonify({"message": "Token is invalid"})

        return f(current_user, *args, **kwargs)
    return decorator


app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "deadbeef"


@app.route("/")
def home():
    return jsonify({"message": "Hello Majfriend, what can I do for You?"})

@app.route("/signup", methods=["POST"])
def signup_user():
    data = request.get_json()
    hashed_password = generate_password_hash(data["password"], method="sha256")

    user_data = {
        "email": data["email"],
        "username": data["username"],
        "password": hashed_password
    }
    mongo_functions.insert_new_user(user_data)
    return jsonify({"message": "Registered successfully"})


@app.route("/signin", methods=["POST"])
def login_user():
    data = request.get_json()

    if not data or not data.get("username") or not data.get("password"):
        return make_response("Could not verify", 401, {"message": "Login required"})

    user = mongo_functions.find_user(data.get("username"))
    pprint.pprint(user)


    if user and check_password_hash(user.get("password"), data.get("password")):
        token = jwt.encode({
            "username": user.get("username"),
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},
            app.config["SECRET_KEY"])

        return jsonify({"token": token,
            "username": user.get("username"),
            "email": user.get("email"),
            "id": user.get("username"),
            "roles": []})

    return make_response(
                jsonify({"message": "User not found"}),
                406
            )

@app.route("/user", methods=["GET"])
@token_required
def user_page(user):
    pprint.pprint(user)
    return jsonify({"message": f"You are correctly authenticated as `{user.get('username')}`"})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
