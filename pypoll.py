# Aims:
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# dependencies
import csv
import os

# Assign variable to take value of path leading to csv to load
file_to_load = os.path.join("Resources","election_results.csv")
# Assign variable to take value of path leading to txt to save output into
file_to_save = os.path.join("analysis", "election_analysis.txt")

# initialize vote counter to 0 before opening file
total_votes = 0

# Declare new list to store candidate names
candidate_options = []

# Declare empty dictionary to store total votes to each candidate as for loop works
candidate_votes = {}

# Open election results and read file, had to specify encoding type to utf-8 because it was defaulting to 1252
with open(file_to_load, encoding='utf-8') as election_data:

    # Read file object with reader function
    file_reader = csv.reader(election_data)
    # Print header row
    headers = next(file_reader)
    print(headers)
    # Print each row in csv file
    for row in file_reader:
        # increment accumulator by 1
        total_votes += 1

        # reference index corresponding to candidate column
        candidate_name = row[2]
        
        # if name is not in options list i.e. if name is unique...
        if candidate_name not in candidate_options:
            # then add it to list
            candidate_options.append(candidate_name)
            # and create key for each candidate, initialize to 0 
            candidate_votes[candidate_name] = 0
        # and increment vote count by 1 when passing through each row
        candidate_votes[candidate_name] += 1
print(candidate_votes)
