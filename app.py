# -*- coding: utf-8 -*-
"""
Created on Sat May 15 23:13:46 2021

@author: xz328e
"""

import pickle
#Line added for git working
# Import all the packages you need for your model below
import numpy as np
import sys
import os
from sklearn.neighbors import KNeighborsClassifier

#os.chdir('C:\Projects\Learning DS\ML_Cloud_Deploy_Example')

# Import Flask for creating API
from flask import Flask, request, render_template

port = int(os.environ.get("PORT", 5000))

# Load the trained model from current directory
with open('./model.pkl', 'rb') as model_pkl:
    knn = pickle.load(model_pkl)

# Initialise a Flask app
app = Flask(__name__)

@app.route('/')
def index1():
    return render_template('index1.html')

# Create an API endpoint
@app.route('/predict', methods=['GET','POST'])
def predict_iris():

    # Read all necessary request parameters
    sl = request.form['sl']
    sw = request.form['sw']
    pl = request.form['pl']
    pw = request.form['pw']
    print('****************')
    print('Input Values:', sl, sw, pl, pw)
    print('****************')
    # Use the predict method of the model to 
    # get the prediction for unseen data
    new_record = np.array([[sl, sw, pl, pw]])
    predict_result = knn.predict(new_record)

    #print('Predicted result for observation ')
    
    
    # return the result back
    prediction = 'Predicted result for observation: ' + str(int(predict_result[0]))
    return render_template('index1.html', predict_result=prediction) 
    #return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')