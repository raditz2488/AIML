from tensorflow.keras.models import load_model
from flask import Flask, request, jsonify
import os
import numpy as np
import uuid

app = Flask(__name__)

