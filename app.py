from flask import Flask, request, render_template
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
model_path = 'model/model.pkl'
if os.path.exists(model_path):
    model = pickle.load(open(model_path, 'rb'))
else:
    model = None
    print("Warning: Model not found. Please run train_model.py first.")


@app.route('/')
def home():
    """Render the home page with the prediction form"""
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """Handle prediction requests"""
    try:
        # Get temperature from form
        temp = float(request.form['temperature'])
        
        # Validate temperature
        if temp < -50 or temp > 150:
            error_msg = "Please enter a temperature between -50 and 150°F"
            return render_template('index.html', error=error_msg)
        
        # Make prediction
        if model:
            prediction = model.predict([[temp]])
            sales = round(prediction[0], 2)
            
            # Ensure non-negative prediction
            if sales < 0:
                sales = 0
            
            return render_template('index.html', 
                                   result=sales, 
                                   temp_input=temp)
        else:
            error_msg = "Model not loaded. Please run train_model.py first."
            return render_template('index.html', error=error_msg)
    
    except ValueError:
        error_msg = "Please enter a valid number for temperature"
        return render_template('index.html', error=error_msg)
    except Exception as e:
        error_msg = f"An error occurred: {str(e)}"
        return render_template('index.html', error=error_msg)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
