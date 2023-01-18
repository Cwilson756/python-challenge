#import modules

import os
import csv 

#create file path to csv
###need to bugfix relative path###
#electionpath = os.path.join("resources", "election_data.csv")
electionpath = r"C:\Users\cwils\OneDrive\Desktop\dabootcamp\python-challenge\PyPoll\resources\election_data.csv"

output =r"C:\Users\cwils\OneDrive\Desktop\dabootcamp\python-challenge\PyPoll\analysis\election_analysis.txt"

#declare variables

new_line = "\n"
tvotes = 0
winner = ""
winning_count = 0

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

#open new txt file to write

with open(output, "w") as f:

    #create election results variable to print and write total votes

    election_results = (f'Election Results{new_line}----------------------------{new_line}Total Votes: {tvotes}{new_line}----------------------------{new_line}')
    print(election_results)
    f.write(election_results)

    #loop through candidate in list to determine vote count and percent per candidate, print out and write

    for candidate in votes: 

        vote_count = votes[candidate]
        
        vote_percentage = float(vote_count) / float(tvotes) * 100
        
        candidate_results = (f'{candidate}: {vote_percentage:.1f}% ({vote_count:,}){new_line}')
        print(candidate_results)
        f.write(candidate_results)

        
        #Determine winner by testing all vote counts against each other and saving candidate as winner
              
        if (vote_count > winning_count): 
    
             winning_count = vote_count
             winner = candidate

    #save winner results string, print and write

    winner_results = (f'-----------------------{new_line}Winner: {winner}{new_line}-----------------------')
    print(winner_results)
    f.write(winner_results)