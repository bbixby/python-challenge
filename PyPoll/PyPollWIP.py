#import modules
import os
import csv
#set local pc path to data csv file
election_csv = os.path.join("..", "..", "election_data.csv")
#create votes dictionary
votes = {}
#votes = dict()
#open and read csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header row
    csv_header = next(csvfile)
    #run through the file
    for row in csvreader:
        #define candidate column
        candidate = row[2]
        #if candidate not in dictionary, add with first vote
        if candidate not in votes:
            votes[candidate] = 1
        #if candidate already in dictionary, add a vote
        else:
            votes[candidate] += 1
#check the results
#for key, value in votes.items():
    #print(f'{key} : {value}')

#add the dictionary keys for vote total
values = votes.values()
voteTotal = sum(values)
#print (voteTotal)

#create the winners, percent, and votes per as a list
#lst=[]
#for key, value in votes.items():
    #lst.append(f"{key}: {value / voteTotal:.3%} ({value})")

#output to terminal and to text file
#output = (
print(f"Election Results\n")
print(f"-------------------------\n")
print(f"Total Votes: {voteTotal}\n")
print(f"-------------------------\n")
    #f"{lst}"
for key, value in votes.items():
    print(f"{key}: {value / voteTotal:.3%} ({value})")
print(f"-------------------------\n")
print(f"Winner: {max(votes, key=votes.get)}\n")
print(f"-------------------------")
    #)
#print(output)

