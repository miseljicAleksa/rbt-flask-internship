from clients_bp import *
from flask_restplus import Resource
from clients_bp import client_bp
from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request,render_template,make_response
from flask.views import View
from clients_bp.models import Client
from app import db

@client_api.route("/", methods=['POST','GET'])
class ClientApi(Resource):

    def post(self):

        headers = {'Content-Type': 'text/html'}
        def helper(arg):
            return make_response(render_template("registration.html",val=arg),200,headers)

        username = request.form["username"]
        password = request.form["password"]

        if None in [password,username]:
            return helper("Fail")

        client = Client(
            username=username,
            password=password
        )

        if db.session.query(Client).filter_by(username=client.username).first() is not None:
            return helper("Used")
            
        db.session.add(client)
        db.session.commit()
        
        return helper("Success")

