from flask import Flask, request, jsonify
from newspapers import *

app = Flask(__name__)

newspaperlist=["milliyet","sabah","takvim"]

@app.route('/newspapers')
def summary():
    return jsonify({"newspapers":newspaperlist})


@app.route('/')
def hello_world():
    return "herald webapi"

@app.route('/milliyet')
def milliyet():
    date=request.args.get('date')
    return getMilliyet(date)

@app.route('/sabah')
def sabah():
    date=request.args.get('date')
    return getSabah(date)

@app.route('/takvim')
def takvim():
    date=request.args.get('date')
    return getTakvim(date)


if __name__ == '__main__':
    app.run()
