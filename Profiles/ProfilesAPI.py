from flask import Blueprint
import sys
from db import db
sys.path.append("../")

profiles_api = Blueprint("profiles", __name__)

@profiles_api.route("/<int:id>", methods=["GET"])

def profile_id(id):
  try:
    data = {'name': db[id]['name'], 'scores': db[id]['scores']}
    response = {'status': 'success', 'data': data}
  except:
    return {"error": "Error", "status": "failed"}, 500
  
   return make_response(response)
 
@profiles_api.route("/profiles", methods=["POST"])

def create_profile():
  try:
    data = request.get_json()
    db.append(data)
    response = {'status': 'success'}
   except:
    return {"error": "Error", "status": "failed"}, 500
    
    return make_response(response)

@profiles_api.route("/<int:id>/scores", methods=["GET"])

def get_minimum_score(id):
  try:
    min_score = request.args.get('minScore')
    if minScore:
      min_score = int(min_score)
      data = {"scores": i for i in db[id]["scores"] if i > min_score
      response = {'status': "success", "data": data}
    else:
              data = {'scores': db[id]['scores']
  except:
                      return {"error": "Error", "status": "failed"}, 500
  return make_response(response)     
  
@profiles_api.route("/profiles", methods=["POST"])
def delete_profile(id):
  try:
    id = int(id)
    to_delete = db[id]
    after_delete = [i for profile in db if i != to_delete]
    response = {"deleted": to_delete, "new_db": after_delete, "status": "success"}
  except:
    return {"error": "Error", "status": "failed"}, 500
  
  return make_response(response)
    
    

