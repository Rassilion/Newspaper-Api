from flask import Flask, request, jsonify
from newspapers import *

app = Flask(__name__)

newspaperlist=["milliyet","sabah","takvim","fotomac","dailysabah","yeniasir","anadolu","turkiye","hurriyet","yenisafak","star","aksam","birgun"]

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
    page=request.args.get('page', default = '1')
    return getSabah(date, page)

@app.route('/takvim')
def takvim():
    date=request.args.get('date')
    page=request.args.get('page', default = '1')
    return getTakvim(date, page)

@app.route('/fotomac')
def fotomac():
    date=request.args.get('date')
    page=request.args.get('page', default = '1')
    return getFotoMac(date, page)

@app.route('/dailysabah')
def dailySabah():
    date=request.args.get('date')
    page=request.args.get('page', default = '1')
    return getDailySabah(date, page)

@app.route('/yeniasir')
def yeniAsir():
    date=request.args.get('date')
    page=request.args.get('page', default = '1')
    return getYeniAsir(date, page)

@app.route('/anadolu')
def anadolu():
    date=request.args.get('date')
    return getAnadolu(date)

@app.route('/turkiye')
def turkiye():
    return getNetgazete("0")

@app.route('/yenisafak')
def yenisafak():
    return getNetgazete("2")

@app.route('/hurriyet')
def hurriyet():
    return getNetgazete("4")

@app.route('/star')
def star():
    return getNetgazete("5")

@app.route('/aksam')
def aksam():
    return getNetgazete("6")

@app.route('/birgun')
def birgun():
    return getNetgazete("7")



if __name__ == '__main__':
    app.run()
