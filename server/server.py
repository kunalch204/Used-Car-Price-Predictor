from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_brand_names',  methods=['GET'])
def get_brand_names():
    response = jsonify({
        'brands': util.get_brand_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_interior_names', methods=['GET'])
def get_interior_names():
    response = jsonify({
        'interiors': util.get_interior_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/get_exterior_names', methods=['GET'])
def get_exterior_names():
    response = jsonify({
        'exteriors': util.get_exterior_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

@app.route('/predict_car_price', methods=['GET', 'POST'])
def predict_car_price():
    brand = request.form['brand']
    interior = request.form['interior']
    exterior = request.form['exterior']
    age = int(request.form['age'])
    miles = int(request.form['miles'])
    accidents = int(request.form['accidents'])
    owners = int(request.form['owners'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(brand, interior, exterior, age, miles, accidents, owners)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == '__main__':
    print('Starting Python Flask Server for Predicting used car prices')
    util.load_saved_artifacts()
    app.run()