# Ice Cream Sales Prediction Web Application

A Flask-based web application that predicts ice cream sales using Linear Regression machine learning model.

## 📁 Project Structure

```
IceCream_Sale/
│
├── static/
│   └── style.css              # CSS styling for the web interface
│
├── templates/
│   └── index.html             # HTML template with prediction form
│
├── model/
│   └── model.pkl              # Trained ML model (generated after train_model.py)
│
├── ice-cream.csv              # Dataset with historical sales data
├── train_model.py             # Script to train the Linear Regression model
├── app.py                     # Flask application entry point
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## 🚀 Quick Start Guide

### Step 1: Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- Flask - Web framework
- pandas - Data manipulation
- scikit-learn - Machine learning library
- numpy - Numerical computing

### Step 2: Train the Model

```bash
python train_model.py
```

This script:
- Loads the ice-cream.csv dataset
- Trains a Linear Regression model using Temperature as input and IceCreamsSold as output
- Saves the trained model to `model/model.pkl`

Expected output:
```
Model trained and saved successfully!
Model coefficient (slope): ~2.XX
Model intercept: ~XX
```

### Step 3: Run the Flask Application

```bash
python app.py
```

Expected output:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Step 4: Access the Web Application

Open your browser and navigate to:
```
http://127.0.0.1:5000
```

## 💡 How to Use the Application

1. **Enter Temperature**: Input the temperature in Fahrenheit in the input field
2. **Click "Predict Sales"**: Submit the form
3. **View Prediction**: The predicted ice cream sales (in units) will be displayed

## 📊 Dataset Description

The `ice-cream.csv` file contains:
- **Date**: Date of the record
- **Temperature**: Temperature in Fahrenheit (feature used for prediction)
- **IceCreamsSold**: Number of ice creams sold (target variable)
- Other columns: DayOfWeek, Month, Rainfall (not used in the current model)

## 🧠 Machine Learning Model

**Algorithm**: Linear Regression

**Formula**: `y = mx + c`

Where:
- y = Predicted Ice Cream Sales
- x = Temperature (input)
- m = Slope (coefficient)
- c = Intercept

The model learns the relationship between temperature and ice cream sales from the training data.

## ✨ Features

- ✅ Simple and intuitive user interface
- ✅ Real-time prediction
- ✅ Input validation (temperature range: -50°F to 150°F)
- ✅ Responsive design (works on desktop and mobile)
- ✅ Error handling with user-friendly messages
- ✅ Beautiful gradient UI with smooth interactions

## 🔧 Customization

### To use multiple features (Temperature + Rainfall):

Edit `train_model.py`:
```python
X = data[['Temperature', 'Rainfall']]  # Use multiple features
y = data['IceCreamsSold']
```

Update `index.html` to add a rainfall input field.

Update `/predict` route in `app.py` to accept rainfall parameter.

### To deploy on a server:

1. Install a production WSGI server: `pip install gunicorn`
2. Run: `gunicorn --bind 0.0.0.0:5000 app:app`
3. Use a reverse proxy like Nginx or Apache

## 📈 Future Enhancements

- Add more features (Humidity, Day of Week, Holiday flag)
- Implement feature scaling for better predictions
- Add data visualization (matplotlib/plotly graphs)
- Deploy on cloud platforms (Heroku, AWS, Google Cloud)
- Add API documentation
- Implement model versioning and retraining
- Add prediction history tracking

## 🐛 Troubleshooting

**Issue**: "Model not found" error
- **Solution**: Run `python train_model.py` first to create the model

**Issue**: Port 5000 is already in use
- **Solution**: Change the port in app.py: `app.run(debug=True, port=5001)`

**Issue**: Template not found error
- **Solution**: Ensure you're running `app.py` from the IceCream_Sale directory

**Issue**: Module not found (pandas, sklearn, etc.)
- **Solution**: Run `pip install -r requirements.txt` again

## 📝 License

This is a learning project. Feel free to modify and extend it as needed.

---

Happy Predicting! 🍦
