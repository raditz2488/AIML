from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify
import os
import numpy as np
import uuid

app = Flask(__name__)

# Boundries for the features
Expected = {'cylinders': {'min': 3, 'max': 8},
 'displacement': {'min': 68.0, 'max': 455.0},
 'horsepower': {'min': 46.0, 'max': 230.0},
 'weight': {'min': 1613, 'max': 5140},
 'acceleration': {'min': 8.0, 'max': 24.8},
 'year': {'min': 70, 'max': 82},
 'origin': {'min': 1, 'max': 3}
 }

# Load the nn model
model = load_model('./mpg_model.h5')

# Create a route
@app.route('/api', methods=['POST'])
def mpg_prediction():
    content = request.json
    errors = []
    # Validation loop for the values to be in range
    for name in content:
        if name in Expected:
            expected_min = Expected[name]['min']
            expected_max = Expected[name]['max']
            value  = content[name]
            if value < expected_min or value > expected_max:
                errors.append(f'Out of bounds: {name}, has a value of: {value}, but it should be between {expected_min} and {expected_max}.')
        else:
            errors.append(f'Unexpected field: {name}.')

    # Loop to check if all expected values are present in the content
    for name in Expected:
        if name not in content:
            errors.append(f'Missing value: {name}')

    # If no errors then return prediction
    # else return error
    if len(errors) < 1:
        X = np.zeros((1,7))
        X[0,0] = content['cylinders']
        X[0,1] = content['displacement']
        X[0,2] = content['horsepower']
        X[0,3] = content['weight']
        X[0,4] = content['acceleration']
        X[0,5] = content['year']
        X[0,6] = content['origin']

        prediction = model.predict(X)

        mpg = float(prediction[0][0])

        response = {'id': str(uuid.uuid4()), "mpg": mpg, "errors": errors}
    else:
        response = {'id': str(uuid.uuid4()), "errors": errors}

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    
