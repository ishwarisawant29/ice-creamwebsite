@echo off
REM Setup script for Ice Cream Sales Prediction Web Application

echo.
echo ================================================
echo Ice Cream Sales Prediction Web App - Setup
echo ================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    pause
    exit /b 1
)

echo [1/3] Installing dependencies...
python -m pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/3] Training the Machine Learning model...
python train_model.py
if %errorlevel% neq 0 (
    echo Error: Failed to train the model
    pause
    exit /b 1
)

echo.
echo [3/3] Starting Flask application...
echo.
echo ================================================
echo Application is running at: http://127.0.0.1:5000
echo Press CTRL+C to stop the server
echo ================================================
echo.

python app.py

pause
