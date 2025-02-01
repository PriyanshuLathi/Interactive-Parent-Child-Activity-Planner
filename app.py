from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    input_data = [
        int(request.form['Olympiad_Participation']),
        int(request.form['Scholarship']),
        int(request.form['School']),
        int(request.form['Grasp_pow']),
        int(request.form['Career_sprt']),
        int(request.form['Act_sprt']),
        int(request.form['Fant_arts']),
        int(request.form['Won_arts']),
        int(request.form['Time_art']),
        int(request.form['age'])
    ]
    
    input_data = np.array(input_data).reshape(1, -1)
    
    prediction = model.predict(input_data)
    
    hobby_mapping = {0: 'Academics', 1: 'Arts', 2: 'Sports'}
    predicted_hobby = hobby_mapping[prediction[0]]
    
    return jsonify({'Predicted Hobby': predicted_hobby})

if __name__ == '__main__':
    app.run(debug=True)
