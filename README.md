# election-analysis

## Project Overview
This script was written to analyze and report the results of an election audit for a US congressional precinct in Colorado. The Election Commission would like the following details reported to certify this congressional race:
* Total number of votes cast
* List of candidates who received votes
* Total number of votes per candidate
* Percentage of votes each candidate won 
* List the winner of the election based on the popular vote

## Resources
Data source: election_results.csv
Software: Python 3.6.1, Visual Studio Code 1.62.3

## Results 
Analysis of the election audit reported, [as printed](https://github.com/dyl-lee/election-analysis/tree/main/analysis) on election_analysis.txt and as printed to terminal:
* There were 369,711 total votes
* The percent of total votes casted in each county were:
  *  Jefferson county: 10.5% of total votes (38,855 votes)
  *  Denver county: 82.8% of total votes (306,055 votes)
  *  Arapahoe county: 6.7% of total votes (24,801 votes)
* Denver was the county with the highest vote count
* The vote breakdown for each candidate were as follows:
  *  Charles Casper Stockham: 23.0% of total votes (85,213 votes)
  *  Diana DeGette: 73.8% of total votes (272,892 votes)
  *  Raymon Anthony Doane: 3.1% of total votes (11,606 votes)
*  The winner of the congressional precinct by popular vote is Diana DeGette with 272,892 votes or 73.8% of the total votes.

## Summary 
This script has the potential to be extended for use beyond the Colorado election. As long as the `csv` file contains vote counts for a given region (state, federal, etc.), variables in `PyPoll.py` involving a region could be modified to something more generic instead of "county". If the format of the `csv` changes, this will require adjustment to which index to extract this regional information. This is possible since `PyPoll.py` appends its county list based on index and the condition that ensures the list only contains unique counties. The general format of the For loop and If conditions is flexible enough to be reused to report supplementary data, as long as the indexes for extraction are adjust as well. Data such as voter demographics or distribution of submitted voting methods (mail-in ballots, punch cards or DRE)  may be informative metrics for any election committee interested in using this script.
