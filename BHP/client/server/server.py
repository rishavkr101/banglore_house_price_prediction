from flask import Flask, request, jsonify
from flask_cors import CORS  # Importing CORS
import util

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for all routes

app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True

@app.route('/get_location_names')  # Correct the URL here
def get_location_names():
    print("in get_location_names")
    response = jsonify({
        'locations': util.get_location_names()  # Make sure this key is 'locations' to match frontend
    })
    return response

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()
