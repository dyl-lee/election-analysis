# Pseudocode
# Total number of votes cast
# A complete list of candidates who received votes
# Total number of votes each candidate received
# Percentage of votes each candidate won
# The winner of the election based on popular vote

# dependencies
import datetime as dt
now = dt.datetime.now()
print("It is currently", now)

# assign variable for file to load and the path as value. We are telling computer to get .csv from Resources folder
file_to_load = 'Resources/election_results.csv'

# open file for reading. Note, variable doesn't need quotes but the mode does
with open(file_to_load) as election_data:

# To do: perform analysis
    print(election_data)
# Close file. Note the syntax for closing is like a method? Closing the file ensures the data is preserved (if read) and any data is stored (if written)
election_data.close()