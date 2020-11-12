from flask import Flask,render_template,url_for,request
import pandas as pd 
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

import pickle

# load the model from disk
filename = 'nlp_model.pkl'
clf = pickle.load(open(filename, 'rb'))
cv=pickle.load(open('tranform.pkl','rb'))
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/predict',methods=['POST'])
def predict():


    if request.method == 'POST':
        message = request.form['message']
        data = message
        k=[]
        for i in range(0,len(data)):
            for j in range(i+1,len(data)+1):
                l=data[i:j]
                k.append(l)
        uniquee=list(set(data))
        o=[]
        for i in k:
            for j in uniquee:
                if j not in i:
                    break
            else:
                o.append(i)
        min_len=len(o[0])
        for i in o:
            if len(i)<min_len:
                min_len=len(i)
        my_prediction=min_len  

    #     vect = cv.transform(data).toarray()
    #     my_prediction = clf.predict(vect)
    return render_template('result.html',prediction = my_prediction)




