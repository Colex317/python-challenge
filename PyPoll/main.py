# Import module to create file path across operating system and the module for reading CSV files:
import os
import csv

# Specify the file path in PyBank file:
election_data = os.path.join("PyPoll", "Resources", "election_data.csv")
election_results = os.path.join("PyPoll", "Analysis", "election_results.txt")

# Define PyBank Budget Data variables and assign values:
total_votes = 0
candidates = {}
max_votes = 0
winner = ""

# Open and read csv file:
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

# Loop through each row of the data:
    for row in csvreader:
        total_votes += 1 # Total number of votes cast:

# List of candidates who receieved votes,their percentage and total votes:
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] = candidates[candidate_name] + 1
        else:
            candidates[candidate_name] = 1

    # Check for the winner based on popular vote
        if candidates[candidate_name] > max_votes:
            max_votes = candidates[candidate_name]
            winner = candidate_name

            # for candidate, votes in candidates.items():
            #     percentage = round((votes / total_votes * 100), 3)

# Print the Election Results:
print("Election Results:")
print("-----------------------------------------------")
print(f"Total Votes: {total_votes}")
print("-----------------------------------------------")
for candidate, votes in candidates.items():
    percentage = round((votes / total_votes * 100), 3)
    print(f"{candidate}: {percentage}% ({votes})")

print("-----------------------------------------------")
print(f"Winner: {winner}")

# Open output and write the result to a textfile:
with open(election_results, 'w') as textfile:
    textfile.write("Election Results:\n")
    textfile.write("-----------------------------------------------\n")
    textfile.write(f"Total Votes: {total_votes}\n")
    textfile.write("-----------------------------------------------\n")
    
    for candidate, votes in candidates.items():
        percentage = round((votes / total_votes * 100), 3)
        textfile.write(f"{candidate}: {percentage}% ({votes})\n")
    
    textfile.write("-----------------------------------------------\n")
    textfile.write(f"Winner: {winner}\n")