from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return {"greeting":"Hello world"}


@app.route('/create', methods=['POST'])
def create():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

@app.route('/delete', methods=['POST', 'GET'])
def delete():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return json
    else:
        return 'Content-Type not supported!'

@app.route('/info/<slug: domine_name>')
def info(domine_name):
    data = request.json
    domine_name = data['domine_name']
    return 'ok'
