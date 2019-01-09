import csv
import pandas

def flipData(filePath, data):
  with open(filePath, mode='w', newline='') as textfile:
    dest = csv.writer(textfile)
    dest.writerow(data[0])
    data = reversed(data[1:])
    for row in data:
      dest.writerow(row)

def importData(filePath):
  # Reverse the order of the data, but retain headder
  reversed_data = list()
  with open(filePath, newline='') as textfile:
    source = csv.reader(textfile)
    reversed_data = list(csv.reader(textfile))

  # Verify data order, if correct don't flip
  if(reversed_data[1][6] > reversed_data[-2][6]):
    flipData(filePath, reversed_data)

  data = pandas.read_csv(filePath, infer_datetime_format=['Time'])
  return data