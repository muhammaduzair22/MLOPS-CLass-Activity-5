from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')
db = client['mydatabase']
collection = db['users']

@app.route('/submit', methods=['POST'])
def submit():
    data = request.form
    name = data['name']
    email = data['email']
    collection.insert_one({'name': name, 'email': email})
    return 'Data inserted successfully.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
