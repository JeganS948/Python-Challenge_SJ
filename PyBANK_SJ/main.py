import os
import csv

csvpath = os.path.join('resources','budget_data.csv')

#Lists to store data
Total_Months = []
Total = []
Average_Change = []
Greatest_Profit_Increase = []
Greatest_Profit_Decrease = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        Total_Months.append(row[1])
        Total.append(row[2])
        Average_Change.append(row[3])
        Greatest_Profit_Increase.append(row[4])
        Greatest_Profit_Decrease.append(row[5])

