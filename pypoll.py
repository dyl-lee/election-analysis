# Pseudocode
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# dependencies
import csv
import os

# cwd was used to test if os.path.join works from cwd. I pasted the Resources folder into C:\Users\dylan and it returned with <_io.TextIOWrapper name='Resources\\election_results.csv' mode='r' encoding='cp1252'>

new_path = 'C:/Users/dylan/OneDrive/Desktop/Class/election-analysis/'

# os.chdir(new_path)
# cwd = os.getcwd()
# print(cwd)

# Assign variable for the file to load and the path using indirect path
file_to_load = os.path.join("Resources", "election_results.csv")

# Open election results and read file, had to specify encoding type to utf-8
with open(file_to_load, encoding='utf-8') as election_data:

    # Print election_data
    print(election_data)
    # after printing I get the exact same return as direct path, not the one as shown in Canvas that starts with <open..>