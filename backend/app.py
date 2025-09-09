from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {
        "id": 1,
        "name": "Chyngyz",
        "age": 20,
        "address": "Some address",
        "data": {
            "email": "chyngyz@example.com",
            "phone": "+996700123456",
            "is_active": True
        }
    },
    {
        "id": 2,
        "name": "Aizada",
        "age": 25,
        "address": "Bishkek, Sovetskaya 45",
        "data": {
            "email": "aizada@example.com",
            "phone": "+996550987654",
            "is_active": False,
            "hobbies": ["reading", "traveling"]
        }
    },
    {
        "id": 3,
        "name": "Nurbek",
        "age": 30,
        "address": "Osh, Lenin 12",
        "data": {
            "email": "nurbek@example.com",
            "phone": "+996770555666",
            "is_active": True,
            "job": "Software Engineer"
        }
    },
    {
        "id": 4,
        "name": "Aigerim",
        "age": 27,
        "address": "Karakol, Issyk-Kul str. 7",
        "data": {
            "email": "aigerim@example.com",
            "phone": "+996701222333",
            "is_active": True,
            "skills": ["Python", "Django", "React"]
        }
    },
    {
        "id": 5,
        "name": "Timur",
        "age": 22,
        "address": "Talas, Central 89",
        "data": {
            "email": "timur@example.com",
            "phone": "+996555444111",
            "is_active": False,
            "favorite_food": "Plov"
        }
    }
]

@app.route('/')
def index():
    return 'Flask app'

@app.route('/users/<int:user_id>')
def hello_world(user_id):
    user = list(filter(lambda t: t['id'] == user_id, users))
    if len(user) == 0:
        return None
    return jsonify(user)

if __name__ == '__main__':
    app.run()
