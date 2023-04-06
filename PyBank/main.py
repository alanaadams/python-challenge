#import modules
import os
import csv
from pathlib import Path
from datetime import datetime

# define file paths
csvpath = Path("Resources/budget_data.csv")
analysispath = Path("analysis/budget_analysis.txt")

#read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read the header row first
    next(csvreader)
     
    #read each row of data after the header
    for row in csvreader: 
        
# sort the data in chronological order (code found on <https://stackoverflow.com/questions/9917865/sorting-a-csv-object-by-dates-in-python>)
        sorted = sorted(csvreader,key=lambda row: datetime.strptime(row[0], "%d-%b"))

# caluclate the number of months included in the set (last date minus first date)
        total_months = csvreader[1][0] - csvreader[86][0]

# calculate the total Profit/Loss over the entire period (sum column 2)
#total_profit_loss = 

# Calculate the changes in profit/loss over the entire period (second profit/loss minus first profit/loss, print in new cell next to second profit/loss, repeat down column)


# Calculate the average change (sum of new column divided by count of new column)
#average_change =  

# Find the max of new column
#max_amount = 

# Find the date of the max of the new column
#max_date = 

# Find the min of new column
#min_amount = 

# Find the date of the min of the new column
#min_date = 

# print to terminal/write the date/amount to analysispath
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
#print(f"Total: ${total_profit_loss}")
#print(f"Average Change: ${average_change}")
#print(f"Greatest Increase in Profits: {max_date} (${max_amount})")
#print(f"Greatest Decrease in Profits: {min_date} (${min_amount})")

analysis = open(budget_analysis.txt,"a")
analysis.write()
analysis.write()
analysis.write()
analysis.write()
analysis.write()
analysis.write()
analysis.write()