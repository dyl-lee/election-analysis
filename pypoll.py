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

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open election results and read file, had to specify encoding type to utf-8 because it was defaulting to 1252
with open(file_to_load, encoding='utf-8') as election_data:

    # Read file object with reader function
    file_reader = csv.reader(election_data)
    # Print header row
    headers = next(file_reader)
    # print(headers)
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

with open(file_to_save, 'w') as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
    )
    print(election_results, end="")
    # save final vote count to text file
    txt_file.write(election_results)
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes)/float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
        # print each candidate's vote info to terminal
        print(candidate_results)

        # save to text file
        txt_file.write(candidate_results)
        # if and combo sets winning count and percentage to the candidate with those votes and percentage. 
        # Is the idea that the for loop will compare each candidate and only overwrite if it satisfies if and?
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
    winning_candidate_summary = (
        f"----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------\n")
       
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    # print winning candidate, vote count and percentage
    # print(f'{winning_candidate} has won the election with {winning_count} votes or {winning_percentage:.1f}% of the popular vote ')
    