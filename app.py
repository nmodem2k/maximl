#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask,render_template,url_for,request



# load the model from disk

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
        o=[]
        for i in k:
            q=set(i)
            o.append(len(q))
        my_prediction=max(o)  

    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




