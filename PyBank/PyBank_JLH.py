#Import modules
import os
import csv

#Define path to data file
budget_csv = os.path.join('.','Resources', 'budget_data.csv')

#Open data file and pass to csvreader
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#Revised to utilize list comprehension
    profit_loss = [int(row[1]) for row in csvreader]
        
with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)       
        
    date = [row[0] for row in csvreader]

#Revise to use list comprehension
change = [profit_loss[i+1] - profit_loss[i] for i in range(len(profit_loss)-1)]


#Use variables to simplify outut
max_profit = (max(change))
min_profit = (min(change))
max_profit_date = date[(change.index(max(change)))+1]
min_profit_date = date[(change.index(min(change)))+1]


#Create and write required output to text file
with open("Financial Analysis.txt", "w") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f'Total Months: {len(date)}', file=f)
    print(f'Total: ${sum(profit_loss)}', file=f)
    print(f'Average Change: ${round((sum(change)/len(change)), 2)}', file=f)
    print(f'Greatest Increase in Profits: {max_profit_date} (${max_profit})', file=f)
    print(f'Greatest Decrease in Profits: {min_profit_date} (${min_profit})', file=f)


#Print required data to terminal
print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(date)}')
print(f'Total: ${sum(profit_loss)}')
print(f'Average Change: ${round((sum(change)/len(change)), 2)}')
print(f'Greatest Increase in Profits: {max_profit_date} (${max_profit})')
print(f'Greatest Decrease in Profits: {min_profit_date} (${min_profit})')
