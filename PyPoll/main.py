import os
import csv

file = 'election_data.csv'

with open(file, newline="") as election_data:
    electionreader = csv.reader(election_data, delimiter=",")

# Read the header row first
    csv_header = next(election_data)
    total_votes = 0
    candidates=[]
    votes=[]
    index = 0

    for row in electionreader:
        total_votes = total_votes+1
        if len(candidates)< 1:  #Adding the first candidate
            candidates.append(row[2])
            votes.append(1)
        elif row[2] not in candidates: #Adding new candidates
            candidates.append(row[2])
            votes.append(1)
        else: #Counting votes for candidates
            index = candidates.index(row[2])
            votes[index]=votes[index]+1
    lines =[]
    lines.append("Election Results")
    lines.append("---------------------------")
    lines.append("Total Votes: " + str(total_votes))
    lines.append("---------------------------")
    index=0
    for names in candidates:
        lines.append(names +  ":" + '{:.3f}%'.format((votes[index]/total_votes)*100) + '({:.0f})'.format(votes[index]))
        index = index +1   
    lines.append("---------------------------")
    max = max(votes)
    index = votes.index(max)
    lines.append("Winner: " + candidates[index])
    lines.append("---------------------------")

    file= open("PyPollResults.txt","w+")
    for items in lines:
        print(items)
        file.write(items)
        file.write("\n") 
    file.close()

