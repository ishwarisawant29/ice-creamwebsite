import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# Load dataset
data = pd.read_csv('ice-cream.csv')

# Extract features (Temperature) and target (IceCreamsSold)
X = data[['Temperature']]
y = data['IceCreamsSold']

# Create and train the model
model = LinearRegression()
model.fit(X, y)

# Create model directory if it doesn't exist
os.makedirs('model', exist_ok=True)

# Save the model
pickle.dump(model, open('model/model.pkl', 'wb'))

print("Model trained and saved successfully!")
print(f"Model coefficient (slope): {model.coef_[0]:.4f}")
print(f"Model intercept: {model.intercept_:.4f}")
