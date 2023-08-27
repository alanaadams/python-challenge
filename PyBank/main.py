#import modules
import os
import csv
from pathlib import Path
from datetime import datetime

# define file paths
csvpath = Path("Resources/budget_data.csv")

# create lists to hold data
profit_loss = []
months = []
row_difference = []
previous_row = 0
max_amount = 0
min_amount = 0
max_date = []
min_date = []

# read csv
with open(csvpath) as csvfile:
    data = csv.reader(csvfile, delimiter=",")
    
    #read the header row first
    next(data)
     
    #read each row of data after the header
    for row in data: 
        
        # add data to months list
        months.append(row[0])

        # add data to total_profit_loss list
        profit_loss.append(int(row[1]))

        # add difference in profit_loss to row_difference
        row_difference.append(int(row[1])+previous_row)

        # if this row amount is greater than the max_amount set this row as max amount and date
        if int(row[1]) > max_amount:
                max_amount = int(row[1])
                max_date = row[0]

        # if this row amount is less than the min_amount set this row as min amount and date
        if int(row[1]) < min_amount:
                min_amount = int(row[1])
                min_date = row[0]

        # assign this row as the previous_row
        previous_row = int(row[1])
        
# caluclate the number of months included in the set (length of months list)
total_months = len(months)

# calculate the total Profit/Loss over the entire period (sum total_profit_loss)
total_profit_loss = sum(profit_loss)

# Calculate the changes in profit/loss over the entire period (second profit/loss minus first profit/loss, print in new cell next to second profit/loss, repeat down column)
total_difference = sum(row_difference)

# Calculate the average change (sum of new column divided by count of new column)
average_difference = total_difference/len(row_difference) 


# print to terminal/write the date/amount to analysispath
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_difference}")
print(f"Greatest Increase in Profits: {max_date} (${max_amount})")
print(f"Greatest Decrease in Profits: {min_date} (${min_amount})")

analysis = open("budget_analysis.txt","a")
analysis.write("Financial Analysis")
analysis.write("\n-------------------------")
analysis.write(f"\nTotal Months: {total_months}")
analysis.write(f"\nTotal: ${total_profit_loss}")
analysis.write(f"\nAverage Change: ${average_difference}")
analysis.write(f"\nGreatest Increase in Profits: {max_date} (${max_amount})")
analysis.write(f"\nGreatest Decrease in Profits: {min_date} (${min_amount})")