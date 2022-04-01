#pyPoll homework

# Import the necessary dependies for os.path.join()
import os
import csv
from queue import Empty

# Read in a .csv file
csv_path = os.path.join("Resources", "election_data.csv")

#improved opening
with open(csv_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

#initialize variables
    ballot_list = []
    unique_candidates = []
    stockham_list = []
    degette_list = []
    doane_list = []

#The total number of votes cast
    for count in csvreader:
        ballot_list.append(count[0])

         #count up ballots for each person
        if "Stockham" in count[2]:
            stockham_list.append(count[2])
                  
        if "DeGette" in count[2]:
            degette_list.append(count[2])
                    
        if "Doane" in count[2]:
            doane_list.append(count[2])

        #A complete list of candidates who received votes
        if count[2] in unique_candidates:
            continue
        else:
            unique_candidates.append(count[2])
        
    


votes = len(ballot_list)
set(unique_candidates)
print(unique_candidates)

stockham = len(stockham_list)
degette = len(degette_list)
doane = len(doane_list)

stockham_pct = round(stockham/votes * 100,3)
degette_pct = round(degette/votes * 100,3)
doane_pct = round(doane/votes * 100,3)
list_count = [stockham, degette, doane]
winner_count = max(list_count)
if winner_count == list_count[0]:
    winner = "Charles Casper Stockham"
if winner_count == list_count[1]:
    winner = "Diana DeGette"
if winner_count == list_count[2]:
    winner = "Raymon Anthony Doane"

#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

print(f"Election Results \n---------------------")
print(f"Total Votes: {votes}\n---------------------") 
print(f"Charles Casper Stockham: {stockham_pct} ({stockham})")
print(f"Diana DeGette: {degette_pct} ({degette})")
print(f"Raymon Anthony Doane: {doane_pct} ({doane})\n---------------------")
print(f"Winner: {winner}\n---------------------")  

#export a text file with the results
output = (
            f"Election Results \n"
            f"---------------------\n"
            f"Total Votes: {votes}\n"
            f"Charles Casper Stockham: {stockham_pct} ({stockham})\n"
            f"Diana DeGette: {degette_pct} ({degette})\n"
            f"Raymon Anthony Doane:  {doane_pct} ({doane})\n"
            f"---------------------\n"
            f"Winner: {winner}\n")
with open('pyPoll.txt','w') as f:
    f.write(output)
