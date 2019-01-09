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