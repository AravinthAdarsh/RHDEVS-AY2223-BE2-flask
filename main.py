from Auth.AuthAPI import auth_api
from Profiles.ProfilesAPI import profiles_api
from flask import Flask
from db import db


@app.route("/", methods=["GET"])
def index():
  return "Welcome to the homepage"

if __name__ == "__main__":
  app.run()

app = Flask(__name__)

app.register_blueprint(profiles_api, url_prefix="/profiles")
app.register_blueprint(auth_api, url_prefix="/auth")
