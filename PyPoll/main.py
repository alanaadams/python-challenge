#import modules
import os
import csv
from pathlib import Path

# define file paths
csvpath = Path("Resources/election_data.csv")
analysispath = Path("analysis/election_analysis.txt")

#read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

# count column 1
# 
# identify unique candidates
# 
# count total votes for each candidate
#
# count total votes
# total_votes = 
# calculate percentage of total votes for each candidate
#
# identify max percentage and which candidate had the max percentage (who won the election) 
#
# print to terminal/write the results to analysispath
# 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidate}: {percent_won}% ({votes_won})")
print("-------------------------")
print("Winner: {winner}")
print("-------------------------")
