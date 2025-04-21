# demo wt and how was used to refer JWT cookies and tokens in SERVER like localhost 

from flask import Flask, request, jsonify
from flask_jwt_extended import (
    JWTManager, create_access_token, get_jwt_identity,
    jwt_required, unset_jwt_cookies, set_access_cookies
)
from datetime import timedelta

app = Flask(__name__)



# Configurations
app.config["JWT_SECRET_KEY"] ='cf6cdec20e1a4236956e945f40872d71'  # Change this!
app.config["JWT_TOKEN_LOCATION"] = ["cookies"]
app.config["JWT_ACCESS_COOKIE_PATH"] = "/"
app.config["JWT_COOKIE_SECURE"] = False  # Set to True in production with HTTPS
app.config["JWT_COOKIE_HTTPONLY"] = True
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

# Dummy user check (replace with DB query in production)
USERS = {
    "admin": "adminpass"
}

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if USERS.get(username) != password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    response = jsonify({"msg": "Login successful"})
    set_access_cookies(response, access_token)
    return response


@app.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"msg": "Logout successful"})
    unset_jwt_cookies(response)
    return response


@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


@app.route("/")
def index():
    return jsonify({"msg": "Welcome to the Flask-JWT backend!"})


if __name__ == "__main__":
    app.run(debug=True)
