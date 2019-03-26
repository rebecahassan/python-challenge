import os
import csv

file = 'budget_data.csv'

with open(file, newline="") as budget_data:
    budgetreader = csv.reader(budget_data, delimiter=",")

# Read the header row first
    csv_header = next(budget_data)
    total_months = 0
    total = 0
    profit = 0
    data=[]
    change=[]
    month=[]
    index = 0


    for row in budgetreader:
        data.append(float(row[1]))
        if len(data) > 1: 
            change.append(float(row[1])-profit)
            month.append(row[0])
        profit = float(row[1])
lines=[]
lines.append("Financial Analysis")
lines.append("----------------------------")
lines.append("Total Months: " + str(len(data)))
lines.append("Total: " +'${:.0f}'.format(sum(data)))
lines.append("Average Change: "+'${:.2f}'.format((data[-1]-data[0])/(len(data)-1)))
max = max(change)   
index = change.index(max)
lines.append("Greatest Increase in Profits: "+ month[index] + '(${:.0f})'.format(max))
min = min(change)
index = change.index(min)
lines.append("Greatest Decrease in Profits: " + month[index] + '(${:.0f})'.format(min))

file= open("PyBankAnalysis.txt","w+")
for items in lines:
 print(items)
 file.write(items)
 file.write("\n")
file.close()