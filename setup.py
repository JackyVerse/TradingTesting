#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Setup script for Trading Simulation Project
Automatically installs required dependencies
"""

import subprocess
import sys
import os

def install_requirements():
    """Install libraries from requirements.txt"""
    print("🔧 Installing required libraries...")
    
    try:
        # Install from requirements.txt
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Installation successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Installation error: {e}")
        return False

def check_python_version():
    """Check Python version"""
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher required!")
        return False
    print(f"✅ Python version: {sys.version}")
    return True

def main():
    print("🚀 Trading Simulation Project Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if install_requirements():
        print("\n🎉 Setup completed! You can now run:")
        print("   python3 trading_simulation.py")
    else:
        print("\n❌ Setup failed!")
        sys.exit(1)

if __name__ == "__main__":
    main() 