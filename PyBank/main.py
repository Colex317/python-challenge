#Import module to create file path across operating system and the module for reading CSV files:
import os
import csv

# Specify the file path in PyBank file:
budget_data = os.path.join("PyBank", "Resources", "budget_data.csv")
financial_analysis = os.path.join("PyBank", "Analysis", "financial_analysis.txt")

# Declare variables:
total_months = 0
net_profit = 0
previous_profit = 0
profit_changes = []

# Variables for greatest increase and decrease:
max_increase = 0
max_increase_month = ""
max_decrease = 0
max_decrease_month = ""

# Open and read csv file:
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# Loop through each row of data:
    for row in csvreader:
       
        total_months += 1 # Total number of months
        net_profit += int(row[1]) # Net total amount of "Profit/Losses"
        
# Changes in "Profit/Losses" over the entire period:       
        current_profit = int(row[1])
        profit_change = current_profit - previous_profit
        previous_profit = current_profit

        profit_changes.append(profit_change)
      
# Greatest decrease  and greatest decrease in profits (date and amount):
        if profit_change > max_increase:
            max_increase = profit_change
            max_increase_month = row[0]
        elif profit_change < max_decrease:
            max_decrease = profit_change
            max_decrease_month = row[0]

# Calculate the average change:
del profit_changes[0]
average_change = round(sum(profit_changes) / len(profit_changes),2)

# Print output:
print("Financial Analysis:")
print("---------------------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${average_change}")
print("Greatest Increase in Profits: ", max_increase_month, "($", max_increase, ")")
print("Greatest Decrease in Profits: ", max_decrease_month, "($", max_decrease, ")")

# Open output and write the result to a textfile:
with open(financial_analysis, 'w') as textfile:
    textfile.write("Financial Analysis:\n")
    textfile.write("---------------------------------------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_profit}\n")
    textfile.write(f"Average Change: ${average_change}\n")
    textfile.write(f"Greatest Increase in Profits: {max_increase_month} (${max_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {max_decrease_month} (${max_decrease})\n")