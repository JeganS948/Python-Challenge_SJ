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
    
#For total months
    for total_months in months:
        totalmonths = total + 1
#For net total
    for total in data:
        total = total+data[1]
#For avergae change
    for average in data:
        average = total/totalmonths
#For greatest increase
    total.sort()
    max = total[-1]
#for greatest decrease
    min = total[0]

print (totalmonths0
print (total)
print (average)
print (max)
print (min)
  
