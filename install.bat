@echo off
REM Trading Simulation Project - Auto Installer for Windows
REM Automatically installs required dependencies

echo 🚀 Trading Simulation Project - Auto Installer
echo ==============================================

REM Check Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python not found!
    echo Please install Python 3.6 or higher
    pause
    exit /b 1
)

echo ✅ Python found:
python --version

REM Check pip
pip --version >nul 2>&1
if errorlevel 1 (
    echo ❌ pip not found!
    echo Please install pip
    pause
    exit /b 1
)

echo ✅ pip found

REM Install requirements
echo 🔧 Installing required libraries...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Installation failed!
    pause
    exit /b 1
)

echo ✅ Installation successful!
echo.
echo 🎉 Setup completed!
echo You can now run: python trading_simulation.py
pause 