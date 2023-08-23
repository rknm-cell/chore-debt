#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import Flask, request, make_response, jsonify, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Resource


# Local imports
from config import app, db, api
# Add your model imports
CORS(app)

db.init_app(app)

# Views go here!

class Chores(Resource):
    def get(self):
        try:
            chores_dict = [chores.to_dict() for chores in Chore.query.all()]
            response = make_response(
                chores_dict,
                200
            )
        except: 
            response = make_response(
                404
            )

api.add_resource(Chores, "/chores")

if __name__ == '__main__':
    app.run(port=5555, debug=True)