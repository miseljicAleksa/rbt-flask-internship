import os
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marshmallow import ValidationError

# if os.environ['ENV_TYPE'] == 'Dev':
#     from config.development import Development as config
# elif os.environ['ENV_TYPE'] == 'Production':
from config.production import Production as config


db = SQLAlchemy()

def create_app(conf):
    app = Flask(__name__)
    app.config.from_object(conf)
    db.init_app(app)

    from measurements_bp import measurement_bp
    app.register_blueprint(measurement_bp)

    from clients_bp import client_bp
    app.register_blueprint(client_bp)

    return app

app = create_app(config)

migrate = Migrate(app, db)

@app.errorhandler(ValidationError)
def _handle_api_error(ex):
    return "Data validation error"

@app.route("/test")
def hello():
    return "Hello world"
@app.route("/")
def regPage():
    return render_template("registration.html",val="Hello")
