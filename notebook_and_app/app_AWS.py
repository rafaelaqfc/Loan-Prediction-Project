# Deploying the model in the cloud

# Importing Flask and jsonify
import flask
from flask import Flask, jsonify, request

# Importing Resource, Api and reqparser
from flask_restful import Resource, Api, reqparse
import pandas as pd
import numpy
import pickle

app = Flask(__name__)
api = Api(app)

class RawFeats:
    def __init__(self, feats):
        self.feats = feats

    def fit(self, X, y=None):
        pass


    def transform(self, X, y=None):
        return X[self.feats]

    def fit_transform(self, X, y=None):
        self.fit(X)
        return self.transform(X)
    
model = pickle.load( open( "logistic_regression_model_tunned.p", "rb" ) )

class Prediction(Resource):
    def post(self):
        if flask.request.method == 'GET':
            return f'Hello, I am working!'
        elif flask.request.method == 'POST':
            json_data = request.get_json()
            df = pd.DataFrame(json_data.values(), index=json_data.keys()).transpose()
            # getting predictions from our model.
            res = model.predict_proba(df)
            # we cannot send numpy array as a result
            return res.tolist() 
    
# Assigning an endpoint
api.add_resource(Prediction, '/predicting')

# Creating an application to be runned independently
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
    
    

    
