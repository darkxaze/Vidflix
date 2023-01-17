from application import app, db
from flask import render_template, request, json, Response, jsonify
from application.models import vid # original
from urllib.request import urlopen
import pickle
import requests
import pandas as pd
from patsy import dmatrices
from config import paypalrestsdk
# from application.models import videos # clode

movies = pickle.load(open('model/movies_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse= True, key=lambda x: x[1])
    recommended_movies_names = []
    for i in distances[1:10]:
        recommended_movies_names.append(movies.iloc[i[0]].title)

    return recommended_movies_names

@app.route("/") # root directory
@app.route("/index") #
@app.route("/home") # 
def videocatalog():
    url = "http://34.116.219.10/myflix/videos"
    response = urlopen(url)
    jdata = json.loads(response.read())   
    # print(jdata)
    for index in jdata:
        # print(index)
        for key in index:
            # print(key,index[key])
            if (key=="thumbnail"):
                thumbnail2 = index[key]
                print(thumbnail2)
            if (key=="title"):
                title2 = index[key]
                print(title2)
    
    videodata = vid.objects.all() # original
    # videodata = videos.objects.all() # cloud
    # return render_template("videocatalog.html", videodata=videodata, data2={"title2":title2, "thumbnail2":thumbnail2}, videocatalog=True)
    # return render_template("videocatalog.html", videodata=videodata, data2=jdata, videocatalog=True)
    return render_template("videocatalog.html", data2=jdata, videocatalog=True)

@app.route('/recommendation', methods = ['GET', 'POST'])
def recommendation():
    movie_list = movies['title'].values
    status = False
    if request.method == "POST":
        try:
            if request.form:
                movies_name = request.form['movies']
                recommended_movies_names = recommend(movies_name)
                status = True

                return render_template("recommend.html", movies_name = recommended_movies_names, movie_list = movie_list, status = status)


        except Exception as e:
            error = {'error': e}
            return render_template("recommend.html",error = error, movie_list = movie_list, status = status)

    else:
        return render_template("recommend.html", movie_list = movie_list, status = status)

@app.route('/payment', methods=['POST'])
def payment():

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:3000/payment/execute",
            "cancel_url": "http://localhost:3000/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "testitem",
                    "sku": "12345",
                    "price": "17.99",
                    "currency": "GBP",
                    "quantity": 1}]},
            "amount": {
                "total": "17.99",
                "currency": "GBP"},
            "description": "This is the payment transaction description."}]})

    if payment.create():
        print('Payment success!')
    else:
        print(payment.error)

    return jsonify({'paymentID' : payment.id})

@app.route('/execute', methods=['POST'])
def execute():
    success = False

    payment = paypalrestsdk.Payment.find(request.form['paymentID'])

    if payment.execute({'payer_id' : request.form['payerID']}):
        print('Execute success!')
        success = True
    else:
        print(payment.error)

    return jsonify({'success' : success})

@app.route("/membership",methods=["GET","POST"]) # 
def membership():
    return render_template("membership.html")

@app.route("/login") # 
def login():
    return render_template("login.html", login=True)

@app.route("/register") # 
def register():
    return render_template("register.html", register=True)

@app.route("/vid1", methods=["GET","POST"]) # 
def vid1():
    url = "http://34.116.219.10/myflix/videos"
    response = urlopen(url)
    jdata = json.loads(response.read())   
    # print(jdata)
    for index in jdata:
        # print(index)
        for key in index:
            # print(key,index[key])
            if (key=="thumbnail"):
                thumbnail2 = index[key]
                print(thumbnail2)
            if (key=="title"):
                title2 = index[key]
                print(title2)

    title = request.args.get('title')
    thumbnail = request.args.get('thumbnail')
    # return render_template("vid1.html", vid1=True, data={"title":title2, "thumbnail":thumbnail2})
    return render_template("vid1.html", vid1=True, data={"title":title, "thumbnail":thumbnail})








