#import modules
import os
import csv
from pathlib import Path

# define file paths
csvpath = Path("Resources/election_data.csv")

# define lists
candidates = ["Charles Casper Stockham", "Diana DeGette", "Raymon Anthony Doane"]
votes1 = []
votes2 = []
votes3 = []

#read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #read the header row first
    next(csvreader)

    #read each row of data after the header
    for row in csvreader: 
        
        # add vote to votes list
        if row[2] == candidates[0]:
            votes1.append(row[2])
        
        if row[2] == candidates[1]:
            votes2.append(row[2])

        if row[2] == candidates[2]:
            votes3.append(row[2])
        
# calculate votes for candidate 1
candidate1 = len(votes1)

# calculate votes for candidate 2
candidate2 = len(votes2)

# calculate votes for candidate 3
candidate3 = len(votes3)

# calculate total votes
total_votes = candidate1 + candidate2 + candidate3

# calculate percentage of total votes for each candidate
percent_won1 = candidate1 / total_votes
percent_won2 = candidate2 / total_votes
percent_won3 = candidate3 / total_votes

# identify max percentage and which candidate had the max percentage (who won the election) 
if percent_won1 > percent_won2 and percent_won1 > percent_won3:
    winner = candidates[0]
elif percent_won2 > percent_won1 and percent_won2 > percent_won3:
    winner = candidates[1]
else:
    winner = candidates[2]

# print to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"{candidates[0]}: {percent_won1}% ({candidate1})")
print(f"{candidates[1]}: {percent_won2}% ({candidate2})")
print(f"{candidates[2]}: {percent_won3}% ({candidate3})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# write the results to analysispath
analysis = open("election_analysis.txt","a")
analysis.write("Election Results")
analysis.write("\n-------------------------")
analysis.write(f"\nTotal Votes: {total_votes}")
analysis.write("\n-------------------------")
analysis.write(f"\n{candidates[0]}: {percent_won1}% ({candidate1})")
analysis.write(f"\n{candidates[1]}: {percent_won2}% ({candidate2})")
analysis.write(f"\n{candidates[2]}: {percent_won3}% ({candidate3})")
analysis.write("\n-------------------------")
analysis.write(f"\nWinner: {winner}")
analysis.write("\n-------------------------")