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

# Open election results and read file, had to specify encoding type to utf-8 because it was defaulting to 1252
with open(file_to_load, encoding='utf-8') as election_data:

    # Read file object with reader function
    file_reader = csv.reader(election_data)
    # Print header row
    headers = next(file_reader)
    print(headers)

