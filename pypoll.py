# Aims:
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# dependencies
import csv
import os

# Assign variable for the file to load and the path using indirect path
file_to_load = os.path.join("Resources","election_results.csv")

# Open election results and read file, had to specify encoding type to utf-8 because it was defaulting to 1252
with open(file_to_load, encoding='utf-8') as election_data:

    # Print election_data
    print(election_data)
    # after printing I get the exact same return as direct path: <_io.TextIOWrapper name='Resources\\election_results.csv' mode='r' encoding='utf-8'>

# Create filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using with statement open election_analysis.txt for writing 
with open(file_to_save, 'w') as txt_file:

    # write in txt_file
    txt_file.write('Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson')