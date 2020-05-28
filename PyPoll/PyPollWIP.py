#import modules
import os
import csv
#set local pc path to data csv file
election_csv = os.path.join("..", "..", "election_data.csv")
#create votes dictionary
votes = {"candidate", "voteCount"}
votes = dict()
#open and read csv
with open(election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #skip the header row
    csv_header = next(csvfile)
    for row in csvreader:
        candidate = row[2]
        if candidate not in votes:
            votes["candidate"] = candidate
            votes["voteCount"] = 1
        else:
            votes["candidate"] = candidate
            votes["voteCount"] = votes["voteCount"] + 1
for key, value in votes.items():
    print(f'{key} : {value}')