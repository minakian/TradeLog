class Stock_Data:
  def __init__(self, stock='', total=0.0, trades=0, shares=0):
    self.stock = stock
    self.total = total
    self.trades = trades
    self.shares = shares
  
  stock = ''
  total = 0.0
  trades = 0
  shares = 0

  income = float()
  total_shares = int()
  average_per_share = float()
  trade_list = list()
  shares = int()
  total_this_trade = float()
  tickets = int()
  comission = float()
  total_comission = float()



# Add Comission to All Areas

## Dashboard
# Date
# Symbol
# Volume - Total for buy/sell
# Executions
# P&L

## Per Trade Breakdown
# Date/Time
# Symbol
# Quantity
# Price
# Position



##### Other #####
# Long vs Short
# Win/Loss
# Win Rankings
# Loss Rankings


### Reports
# Average Per-Trade Performance

## Statistics ##
# Total Gain/Loss
# Average Daily Gain/Loss
# Average Daily Volume
# Average Winning Trade
# Average Losing Trade
# Total Trades
# Number of Winning Trades
# Number of Losing Trades
# Max Consecutive Wins
# Largest Gain
# Largest Loss
# Average Per-Share gain/loss
# Average Trade Gain/Loss
# Trade P&L Standard Deviation
# Profit Factor
# Average Hold Time (Winning Trades)
# Average Hold Time (Losing Trades)
# Max Consecutive Loses

### Filtering ###
# Symbol
# Tag
# Side (Long/Short)
# Duration
# Date Range
