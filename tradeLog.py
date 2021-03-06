import csv
import pandas
import sys
import os
import matplotlib.pyplot as plt

import StockData as sd
import DataImporting as di

#nvda = SD.Stock_Data('NVDA', 1.0, 3, 5)

# TODO: Use class to track specific trades - Traded multiple stocks at the same time created issues
# TODO: Track long/short bias, profit diff

def trackTrades(data):
  income = float()
  total_shares = int()
  average_per_share = float()
  trade_list = list()
  shares = int()
  total_this_trade = float()
  tickets = int()
  comission = float()
  total_comission = float()

  print()
  print(len(data.index), end='')
  print(' number of entries')
  for i in range(0,len(data.index)):
    # Count tickets
    if data['Event'][i] == 'Accept':
      tickets += 1
      if data['Event'][i+1] == 'Execute':
        comission = data['Shares'][i] * 0.005
        if comission < 1:
          comission = 1
        total_comission += comission
    # Track Shares, Total Shares, Total $ this trade, Total $
    if data['Event'][i] == 'Execute':
      if data['B/S'][i] == 'Buy':
        total_shares += data['Shares'][i]
        shares += data['Shares'][i]
        total_this_trade += data['Shares'][i] * -1 * data['Price'][i]
        income += data['Shares'][i] * -1 * data['Price'][i]
      else:
        income += data['Shares'][i] * data['Price'][i]
        shares += data['Shares'][i] * -1
        total_this_trade += data['Shares'][i] * data['Price'][i]
      # Add trade to trade list
      if shares == 0:
        trade_list.append(total_this_trade)
        total_this_trade = 0

  print('$' + "%.2f" % income, end='')
  print(' income')
  print('%i' %tickets + ' total trades') 
  print('%i' %total_shares + ' total shares')
  print('$' + '%.3f' %(income/total_shares) + '/share')
  print(trade_list, end='')
  print(' trade list')
  print(total_comission, end='')
  print(' total comission')
  return income, total_comission


if __name__ == '__main__':
  data = list(pandas.core.frame.DataFrame())

  track_total = list()
  
  directory = os.getcwd()
  directory += 'Files/'
  for root,dirs,files in os.walk(directory):
    print(root)
    files.sort()
    for file in files:
       if file.endswith(".csv"):
         print(file)
         data.append(di.importData(root + file))

  print(data)
  income, comission = float(), float()
  total_income = 25000.0
  total_comission = 0.0

  track_total.append(total_income)

  for data_set in data:
    income, comission = trackTrades(data_set)
    print('$' + '%.2f' %income + ' $' + '%.2f' %comission + ' $' + '%.2f'%(income-comission))
    total_income += income
    total_comission += comission
    track_total.append((total_income - total_comission))

  print('$' + '%.2f - ' %total_income + '$' + '%.2f = ' %total_comission + '$' + '%.2f'  %(total_income - total_comission))
  print(track_total)

  plt.plot(track_total)
  #plt.axis([0, 6, track_total[0]*.95, track_total[-1]*1.05])
  plt.show()


# What kind of analysis should be available
#   Total account value
#   Total profit/loss per:
#       Day
#       Stock
#       Share
#       Trade
#
#   Total investment per trade
#   Long vs Short:
#     Bias
#     Profit/Loss
