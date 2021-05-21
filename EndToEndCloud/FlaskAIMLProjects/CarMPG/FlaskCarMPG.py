from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify
import os
import numpy as np
import uuid

app = Flask(__name__)

Expected = {'cylinders': {'min': 3, 'max': 8},
 'displacement': {'min': 68.0, 'max': 455.0},
 'horsepower': {'min': 46.0, 'max': 230.0},
 'weight': {'min': 1613, 'max': 5140},
 'acceleration': {'min': 8.0, 'max': 24.8},
 'year': {'min': 70, 'max': 82},
 'origin': {'min': 1, 'max': 3}
 }

 model = load_model('./mpg_model.h5')

 