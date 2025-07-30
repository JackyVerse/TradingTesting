#!/bin/bash
# -*- coding: utf-8 -*-
# Trading Simulation Project - Auto Installer
# Automatically installs required dependencies

echo "🚀 Trading Simulation Project - Auto Installer"
echo "=============================================="

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found!"
    echo "Please install Python 3.6 or higher"
    exit 1
fi

echo "✅ Python3 found: $(python3 --version)"

# Check pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 not found!"
    echo "Please install pip3"
    exit 1
fi

echo "✅ pip3 found"

# Install requirements
echo "🔧 Installing required libraries..."
if pip3 install -r requirements.txt; then
    echo "✅ Installation successful!"
    echo ""
    echo "🎉 Setup completed!"
    echo "You can now run: python3 trading_simulation.py"
else
    echo "❌ Installation failed!"
    exit 1
fi 