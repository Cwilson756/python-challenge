#import modules

import os
import csv 

#create file path to csv

#electionpath = os.path.join("Resources", "election_data.csv")
electionpath = r"C:\Users\cwils\OneDrive\Desktop\dabootcamp\python-challenge\PyPoll\Resources\election_data.csv"

#declare variables

new_line = "\n"
tvotes = 0
winner = ""

#create candidate list and votes dictionary

candidates = []
votes = {}

#open and read csv file

with open(electionpath, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header_row = next(csv_file)

    #loop through rows in the CSV file

    for row in csv_reader:

        #count rows to determine total votes

        tvotes = tvotes + 1

        name = row[2]

        if name not in candidates: 
            
            candidates.append(name)
             
            votes[name] = 0

        votes[name] += 1


#print out election results  

#print(f'Election Results{new_line}----------------------------{new_line}Total Votes: {tvotes}{new_line}----------------------------{new_line}Charles Casper Stockham:{stockhampercent}% ({stockhamvote}){new_line}Diana DeGette:{degettepercent}% ({degettevote}){new_line}Raymon Anthony Doane:{doanepercent}% ({doanevote}){new_line}----------------------------{new_line}Winner: {winner}{new_line}----------------------------{new_line}')

# #export text file with results
# with open("results.txt", "w") as f:
#     f.write("hi")