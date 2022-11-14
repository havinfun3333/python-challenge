# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


csvpath = os.path.join(r'C:\Users\Peter\Source\Repos\python-challenge\PyPoll', 'Resources', 'election_data.csv')

# Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)

    # Set initial value of the total votes
    total_votes = 0

    # Create the list of all the candidates who received votes and vote list
    candidates = []
    vote_list = []

    # Use for loop to go through the file
    for row in csvreader:

        # we add all the candidate into the vote_list and increase the value of total votes by 1
        vote_list.append(row[2])
        total_votes = total_votes + 1

        # if the candidate is not the list of candidates we add it into the list
        if row[2] not in candidates:
            candidates.append(row[2])

# Create the dictionary for the candidates and their number of votes
result_list = {}

# after we get the list of candidates, we loop through the list to find out how many votes they got
for candidate in candidates:
    result_list.update({f"{candidate}": [vote_list.count(candidate)/total_votes, vote_list.count(candidate)]})


# winner has the highest number of votes which is the mode of the vote_list third column of the file
winner = max(result_list, key=result_list.get)

# Print out the result in terminal
print("Election Results")
print("--------------------------------")
print(f"Total votes: {total_votes} ")
print("--------------------------------" )
for candidate in candidates:
    print(f"{candidate}: {round(result_list[candidate][0],5) * 100}% ({result_list[candidate][1]})")
print("--------------------------------")
print(f"Winner: {winner}")
print("--------------------------------")



# Export the analysis results to a text file
with open(os.path.join(r"C:\Users\Peter\Source\Repos\python-challenge\PyPoll\analysis","pyroll.txt"),"w") as f:
    f.write("Election Results" "\n")
    f.write("--------------------------------""\n")
    f.write(f"Total votes: {total_votes} ""\n")
    f.write("--------------------------------" "\n")
    for candidate in candidates:
        f.write(f"{candidate}: {round(result_list[candidate][0],5)*100}% ({result_list[candidate][1]})     \n")

    f.write("--------------------------------""\n")
    f.write(f"Winner: {winner}" "\n")
    f.write("--------------------------------""\n")
