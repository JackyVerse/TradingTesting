# Trading Simulation Project

Financial trading simulation with customizable parameters for backtesting and analysis.

## 📋 System Requirements

- Python 3.6 or higher
- pip (Python package installer)

## 🚀 Quick Installation

### Method 1: Automatic Installation (Recommended)

**On macOS/Linux:**
```bash
chmod +x install.sh
./install.sh
```

**On Windows:**
```cmd
install.bat
```

### Method 2: Manual Installation

```bash
pip3 install -r requirements.txt
```

### Method 3: Using Setup Script

```bash
python3 setup.py
```

## ⚙️ Configuration Setup

### Option 1: Interactive Configuration Creator (Recommended)
```bash
python3 create_config.py
```
This will guide you through creating your first configuration file with interactive prompts.

### Option 2: Manual Configuration
1. Copy the example configuration:
   ```bash
   cp config_example.json config.json
   ```
2. Edit `config.json` with your preferred settings

### Option 3: Use Default Configuration
The program will automatically create a default `config.json` if none exists.

## 🎮 Usage

1. **Run Simulation:**
   ```bash
   python3 trading_simulation.py
   ```

2. **Customize Parameters:**
   Edit `config.json` to modify simulation parameters:
   ```json
   {
       "trading_config": {
           "initial_capital": 10000,      // Starting capital
           "n_trades": 100000,            // Number of trades
           "win_rate": 0.4,               // Win probability (0.0-1.0)
           "risk_per_trade": 0.01,        // Risk per trade (1% = 0.01)
           "reward_per_trade": 0.02       // Reward per winning trade (2% = 0.02)
       },
       "output_config": {
           "log_directory": "trading_sim_logs",
           "save_summary": true,
           "save_trades": true,
           "save_chart": true,
           "chart_size": [12, 6]
       },
       "simulation_config": {
           "random_seed": null,           // Set to number for reproducible results
           "enable_progress_bar": true,
           "decimal_places": 2
       }
   }
   ```

## 📊 Output Results

After running, the program will generate:

- **Summary Report:** `trading_sim_logs/summary_[timestamp].csv`
- **Trade History:** `trading_sim_logs/trades_[timestamp].csv`
- **Equity Curve Chart:** `trading_sim_logs/equity_curve_[timestamp].png`

## 📦 Dependencies

- `numpy`: Numerical computations
- `pandas`: Data manipulation and analysis
- `matplotlib`: Chart generation and visualization

## 🔧 Troubleshooting

If you encounter issues, try:

1. **Update pip:**
   ```bash
   pip3 install --upgrade pip
   ```

2. **Reinstall libraries:**
   ```bash
   pip3 uninstall numpy pandas matplotlib
   pip3 install -r requirements.txt
   ```

3. **Check Python version:**
   ```bash
   python3 --version
   ```

4. **Reset configuration:**
   ```bash
   python3 create_config.py
   ```

## 📝 Notes

- Ensure write permissions in the current directory
- Results are saved in the `trading_sim_logs` folder
- Each run creates new files with unique timestamps
- The simulation uses Monte Carlo methods for realistic trading scenarios

## 🎯 Features

- **External Configuration:** Easy-to-edit JSON configuration file
- **Interactive Setup:** Guided configuration creation
- **Monte Carlo Simulation:** Random trade generation based on win rate
- **Risk Management:** Configurable risk per trade
- **Performance Metrics:** Win rate, profit factor, expectancy calculation
- **Visualization:** Equity curve charts for analysis
- **Data Export:** CSV files for further analysis in Excel or other tools
- **Progress Tracking:** Real-time simulation progress
- **Validation:** Automatic configuration validation

## 📈 Performance Metrics

The simulation calculates:
- **Win Rate:** Percentage of winning trades
- **Profit Factor:** Ratio of gross profit to gross loss
- **Expectancy:** Expected profit/loss per trade
- **Final Capital:** Ending balance after all trades

## 🎲 Trading Scenarios

Pre-configured scenarios available in `config_example.json`:
- **Conservative:** High win rate (60%), low risk (1%), moderate reward (1.5%)
- **Balanced:** Medium win rate (50%), balanced risk/reward (1.5%/2.5%)
- **Aggressive:** Low win rate (30%), high risk (2%), high reward (4%)

## 🔄 Configuration Management

- **Backup Configs:** Save different configurations for different strategies
- **Version Control:** Track configuration changes with git
- **Validation:** Automatic parameter validation prevents invalid settings
- **Flexibility:** Enable/disable output options as needed 