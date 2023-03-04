# Deploying the model in the cloud
from flask import Flask, request, jsonify
import joblib

# Loading the Logistic Regressor model
pipeline_loaded = joblib.load('logistic_model.joblib')

# Creating a Flask application
app = Flask(__name__)

# Defining a route for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json  # Get the input data from the request
    output_data = pipeline_loaded.predict(input_data) # Make a prediction using the loaded model
    return jsonify(output_data) # Return the prediction as JSON

# Starting the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)

    