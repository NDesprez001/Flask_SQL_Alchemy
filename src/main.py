"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, Users, Jobs
import seeds
import db_add_zip
import ex_file
#from models import Person


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "hello": "world"
    }

    return jsonify(response_body), 200

@app.route('/popultate_database', methods=['GET'])
def pop_data():
    return seeds.run()

@app.route('/zip_info', methods=['POST'])
def zip_info():
    return db_add_zip.make_table()

@app.route('/users/<id>', methods=['POST', 'GET'])
def get_users_id(id):
    # user = Users.query.get(1)
    # user_dict = user.serialize()
    if not id.isnumeric():
        return 'ID must be numeric'
    
    user = Users.query.get(int(id))
        
    if user is None:
        return 'User not found'
    
    return jsonify(user.serialize())

@app.route('/user', methods = ['POST', 'GET'])
def get_user():
    users = Users.query.filter(Users.username.ilike('%a%'))
    return (jsonify([(x.serialize()) for x in users]))

# @app.route('/numbers', methods = ['POST', 'GET'])
# def odd():
#     lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#     new_lst = []
#     for i in lst:
#         if i%2 == 0:
#         new_lst.append(i)
#     return new_lst

@app.route('/ex', methods = ['POST', 'GET'])
def new_table():
    return ex_file.ex_run()




@app.route('/ex_1/<id_1>', methods = ['POST'])
def ex_1(id_1):
    
    j_info = Jobs.query.get(int(id_1))
        
    if j_info is None:
        return 'Job not found'
    
    return jsonify(j_info.serialize())

@app.route('/ex_2/<id_2>', methods = ['GET'])
def ex_2(id_2):
    j_info = Jobs.query.get(int(id_2))
        
    if j_info is None:
        return 'Job not found'
    
    return jsonify(j_info.serialize())

# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
