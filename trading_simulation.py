
# -*- coding: utf-8 -*-
import os
import json
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def load_config(config_file="config.json"):
    """Load configuration from JSON file"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print(f"✅ Configuration loaded from {config_file}")
        return config
    except FileNotFoundError:
        print(f"❌ Configuration file {config_file} not found!")
        print("Please create config.json or copy from config_example.json")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error reading configuration file: {e}")
        return None

def validate_config(config):
    """Validate configuration parameters"""
    if not config:
        return False
    
    # Check required sections
    required_sections = ['trading_config', 'output_config', 'simulation_config']
    for section in required_sections:
        if section not in config:
            print(f"❌ Missing required section: {section}")
            return False
    
    # Validate trading config
    trading = config['trading_config']
    if trading['initial_capital'] <= 0:
        print("❌ Initial capital must be positive")
        return False
    if trading['n_trades'] <= 0:
        print("❌ Number of trades must be positive")
        return False
    if not (0 <= trading['win_rate'] <= 1):
        print("❌ Win rate must be between 0 and 1")
        return False
    if trading['risk_per_trade'] <= 0:
        print("❌ Risk per trade must be positive")
        return False
    if trading['reward_per_trade'] <= 0:
        print("❌ Reward per trade must be positive")
        return False
    
    return True

def run_simulation(config):
    """Run the trading simulation with given configuration"""
    trading_config = config['trading_config']
    output_config = config['output_config']
    sim_config = config['simulation_config']
    
    # Set random seed if specified
    if sim_config['random_seed'] is not None:
        np.random.seed(sim_config['random_seed'])
        print(f"🔧 Using random seed: {sim_config['random_seed']}")
    
    # Create log directory
    log_dir = output_config['log_directory']
    os.makedirs(log_dir, exist_ok=True)
    
    print(f"🚀 Starting simulation with {trading_config['n_trades']} trades...")
    
    # Generate random win/loss results based on probability
    results = np.random.choice([1, 0], size=trading_config['n_trades'], 
                              p=[trading_config['win_rate'], 1 - trading_config['win_rate']])
    
    # Simulate capital flow
    capital = [trading_config['initial_capital']]
    trade_log = []
    
    for i, result in enumerate(results):
        prev_capital = capital[-1]
        if result == 1:
            profit = prev_capital * trading_config['reward_per_trade']
            new_capital = prev_capital + profit
            outcome = "Win"
        else:
            loss = prev_capital * trading_config['risk_per_trade']
            new_capital = prev_capital - loss
            outcome = "Loss"
        
        capital.append(new_capital)
        trade_log.append({
            "Trade": i + 1,
            "Result": outcome,
            "Capital_Before": round(prev_capital, sim_config['decimal_places']),
            "Capital_After": round(new_capital, sim_config['decimal_places']),
            "Profit_Loss": round(new_capital - prev_capital, sim_config['decimal_places'])
        })
        
        # Show progress every 10% if enabled
        if sim_config['enable_progress_bar'] and (i + 1) % (trading_config['n_trades'] // 10) == 0:
            progress = ((i + 1) / trading_config['n_trades']) * 100
            print(f"📊 Progress: {progress:.0f}%")
    
    # Calculate results summary
    n_wins = np.sum(results)
    n_losses = trading_config['n_trades'] - n_wins
    final_capital = capital[-1]
    profit_factor = (n_wins * trading_config['reward_per_trade']) / (n_losses * trading_config['risk_per_trade']) if n_losses > 0 else float('inf')
    expectancy = trading_config['win_rate'] * trading_config['reward_per_trade'] + (1 - trading_config['win_rate']) * (-trading_config['risk_per_trade'])
    
    summary = pd.DataFrame({
        "Winning_Trades": [n_wins],
        "Losing_Trades": [n_losses],
        "Win_Rate_Percent": [round(n_wins / trading_config['n_trades'] * 100, sim_config['decimal_places'])],
        "Final_Capital": [round(final_capital, sim_config['decimal_places'])],
        "Profit_Factor": [round(profit_factor, sim_config['decimal_places'])],
        "Expectancy_Percent": [round(expectancy * 100, sim_config['decimal_places'])],
    })
    
    # Save files based on output configuration
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    saved_files = []
    
    if output_config['save_summary']:
        summary_file = os.path.join(log_dir, "summary_{}.csv".format(timestamp))
        summary.to_csv(summary_file, index=False)
        saved_files.append(("Summary", summary_file))
    
    if output_config['save_trades']:
        trades_file = os.path.join(log_dir, "trades_{}.csv".format(timestamp))
        pd.DataFrame(trade_log).to_csv(trades_file, index=False)
        saved_files.append(("Trade History", trades_file))
    
    if output_config['save_chart']:
        chart_file = os.path.join(log_dir, "equity_curve_{}.png".format(timestamp))
        plt.figure(figsize=tuple(output_config['chart_size']))
        plt.plot(capital, label="Capital over time")
        plt.title("Trading Simulation - Capital Growth")
        plt.xlabel("Trade Number")
        plt.ylabel("Capital (USD)")
        plt.grid(True)
        plt.legend()
        plt.tight_layout()
        plt.savefig(chart_file)
        plt.close()
        saved_files.append(("Equity Chart", chart_file))
    
    # Output results
    print("\n✅ Simulation completed successfully!")
    for file_type, file_path in saved_files:
        print(f"📊 {file_type} saved to: {file_path}")
    
    return summary, trade_log, capital

def main():
    """Main function"""
    print("🚀 Trading Simulation Project")
    print("=" * 50)
    
    # Load configuration
    config = load_config()
    if not config:
        return
    
    # Validate configuration
    if not validate_config(config):
        print("❌ Invalid configuration!")
        return
    
    # Run simulation
    summary, trade_log, capital = run_simulation(config)
    
    # Display summary
    print("\n📈 SIMULATION SUMMARY:")
    print("=" * 30)
    for col in summary.columns:
        print(f"{col}: {summary[col].iloc[0]}")

if __name__ == "__main__":
    main()
