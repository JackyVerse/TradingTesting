#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Configuration File Creator
Helps users create their first config.json file
"""

import json
import os

def create_default_config():
    """Create default configuration file"""
    default_config = {
        "trading_config": {
            "initial_capital": 10000,
            "n_trades": 100000,
            "win_rate": 0.4,
            "risk_per_trade": 0.01,
            "reward_per_trade": 0.02
        },
        "output_config": {
            "log_directory": "trading_sim_logs",
            "save_summary": True,
            "save_trades": True,
            "save_chart": True,
            "chart_size": [12, 6]
        },
        "simulation_config": {
            "random_seed": None,
            "enable_progress_bar": True,
            "decimal_places": 2
        }
    }
    
    return default_config

def create_scenario_configs():
    """Create different trading scenario configurations"""
    scenarios = {
        "conservative": {
            "initial_capital": 10000,
            "n_trades": 100000,
            "win_rate": 0.6,
            "risk_per_trade": 0.01,
            "reward_per_trade": 0.015
        },
        "balanced": {
            "initial_capital": 10000,
            "n_trades": 100000,
            "win_rate": 0.5,
            "risk_per_trade": 0.015,
            "reward_per_trade": 0.025
        },
        "aggressive": {
            "initial_capital": 10000,
            "n_trades": 100000,
            "win_rate": 0.3,
            "risk_per_trade": 0.02,
            "reward_per_trade": 0.04
        }
    }
    
    return scenarios

def main():
    """Main function"""
    print("🔧 Configuration File Creator")
    print("=" * 40)
    
    # Check if config.json already exists
    if os.path.exists("config.json"):
        print("⚠️  config.json already exists!")
        response = input("Do you want to overwrite it? (y/N): ").lower()
        if response != 'y':
            print("❌ Operation cancelled")
            return
    
    # Create default config
    config = create_default_config()
    
    # Ask user for preferences
    print("\n📝 Let's customize your configuration:")
    
    # Trading parameters
    print("\n💰 Trading Parameters:")
    try:
        config['trading_config']['initial_capital'] = float(input("Initial capital (default 10000): ") or 10000)
        config['trading_config']['n_trades'] = int(input("Number of trades (default 100000): ") or 100000)
        config['trading_config']['win_rate'] = float(input("Win rate 0.0-1.0 (default 0.4): ") or 0.4)
        config['trading_config']['risk_per_trade'] = float(input("Risk per trade 0.01=1% (default 0.01): ") or 0.01)
        config['trading_config']['reward_per_trade'] = float(input("Reward per trade 0.02=2% (default 0.02): ") or 0.02)
    except ValueError:
        print("❌ Invalid input! Using default values.")
    
    # Output preferences
    print("\n📊 Output Preferences:")
    config['output_config']['save_summary'] = input("Save summary report? (Y/n): ").lower() != 'n'
    config['output_config']['save_trades'] = input("Save trade history? (Y/n): ").lower() != 'n'
    config['output_config']['save_chart'] = input("Save equity chart? (Y/n): ").lower() != 'n'
    
    # Simulation preferences
    print("\n⚙️  Simulation Preferences:")
    config['simulation_config']['enable_progress_bar'] = input("Show progress bar? (Y/n): ").lower() != 'n'
    
    # Save configuration
    try:
        with open("config.json", 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print("\n✅ Configuration saved to config.json")
        print("🚀 You can now run: python3 trading_simulation.py")
    except Exception as e:
        print(f"❌ Error saving configuration: {e}")

if __name__ == "__main__":
    main() 