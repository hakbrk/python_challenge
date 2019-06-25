import os
import csv

budget_csv = os.path.join('.','Resources', 'budget_data.csv')

with open(budget_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    profit_loss = []
    date = []
    for row in csvreader:
        profit_loss.append(int(row[1]))
        date.append(row[0])

change = []
for i in range(1, len(profit_loss)):
    change.append(profit_loss[i]-profit_loss[i-1])

max_profit = (max(change))
min_profit = (min(change))
max_profit_date = date[(change.index(max(change)))+1]
min_profit_date = date[(change.index(min(change)))+1]


with open("Financial Analysis.txt", "w") as f:
    print("Financial Analysis", file=f)
    print("----------------------------", file=f)
    print(f'Total Months: {len(date)}', file=f)
    print(f'Total: ${sum(profit_loss)}', file=f)
    print(f'Average Change: ${round((sum(change)/len(change)), 2)}', file=f)
    print(f'Greatest Increase in Profits: {max_profit_date} (${max_profit})', file=f)
    print(f'Greatest Decrease in Profits: {min_profit_date} (${min_profit})', file=f)

print("Financial Analysis")
print("----------------------------")
print(f'Total Months: {len(date)}')
print(f'Total: ${sum(profit_loss)}')
print(f'Average Change: ${round((sum(change)/len(change)), 2)}')
print(f'Greatest Increase in Profits: {max_profit_date} (${max_profit})')
print(f'Greatest Decrease in Profits: {min_profit_date} (${min_profit})')
