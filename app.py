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
	

    return render_template('result.html',prediction = min_len)



if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




