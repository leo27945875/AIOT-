from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/test"
mongo = PyMongo(app)


@app.route('/members')
@app.route('/member/<id>', methods = ['GET'])
def GetMember(id=None):
    if id is None:
        members = mongo.db.member.find({})
        result = []
        for member in members:
            member['_id'] = str(member['_id'])
            result.append(member)

        return jsonify(result)
    else:
        result = mongo.db.member.find_one({'_id': ObjectId(id)})
        if result is not None:
            result['_id'] = str(result['_id'])
        
        return jsonify(result)


@app.route('/members', methods = ['POST'])
def AddMember():
    name = request.form.get('name')
    age = request.form.get('age')
    phone = request.form.get('phone')
    email = request.form.get('email')

    data = {'name': name, 'age': age, 'phone': phone, 'email': email}
    result = mongo.db.member.insert_one(data)
    return str(result.inserted_id)


@app.route('/members/<id>', methods = ['DELETE'])
def RemoveMember(id):
    member = mongo.db.member.find_one({'_id': ObjectId(id)})
    if member:
        del_result = mongo.db.member.delete_one(member)

    result = del_result.deleted_count if del_result else 0

    return "Delete %s data" % str(result)


@app.route('/members/<id>', methods = ['PUT'])
def UpdateMember(id):
    name = request.form.get('name')
    age = request.form.get('age')
    phone = request.form.get('phone')
    email = request.form.get('email')
    
    newValue = { "$set": { "name": name, "age": age, "phone": phone, "email": email } }
    updResult = mongo.db.member.update_one({"_id": ObjectId(id)}, newValue)
    result = updResult.modified_count if updResult else 0
    
    # 回傳更新的資料筆數
    return "Update %s data" % str(result)


if __name__ == "__main__":
    app.run()