# Configuration Guide

## TRADING_CONFIG:
- `initial_capital`: Starting capital in USD
- `n_trades`: Number of trades to simulate
- `win_rate`: Probability of winning a trade (0.0 to 1.0)
- `risk_per_trade`: Risk per trade as percentage of current capital (0.01 = 1%)
- `reward_per_trade`: Reward per winning trade as percentage of current capital (0.02 = 2%)

## OUTPUT_CONFIG:
- `log_directory`: Directory to save output files
- `save_summary`: Whether to save summary report
- `save_trades`: Whether to save detailed trade history
- `save_chart`: Whether to save equity curve chart
- `chart_size`: Chart dimensions [width, height] in inches

## SIMULATION_CONFIG:
- `random_seed`: Set to a number for reproducible results, null for random
- `enable_progress_bar`: Show progress during simulation
- `decimal_places`: Number of decimal places for output values

## EXAMPLE SCENARIOS:

### Conservative Strategy
```json
{
    "win_rate": 0.6,
    "risk_per_trade": 0.01,
    "reward_per_trade": 0.015
}
```

### Balanced Strategy
```json
{
    "win_rate": 0.5,
    "risk_per_trade": 0.015,
    "reward_per_trade": 0.025
}
```

### Aggressive Strategy
```json
{
    "win_rate": 0.3,
    "risk_per_trade": 0.02,
    "reward_per_trade": 0.04
}
``` 