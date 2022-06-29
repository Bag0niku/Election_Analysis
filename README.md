# Election_Analysis

## Project Overview
A Colorado Board of Elections employee has given me the following tasks to complete the election audit of a recent local congressional election.

 1) Calculate the total number of votes cast.
 2) Get a complete list of candidates who received votes.
 3) Calculate the total number of votes each candidate received.
 4) Calculate the the percentage of votes each candidate won.
 5) Determine the winner of the election based on popular vote.

### Resources
- Data Source: election_results.csv
- Software: Python 3.8.13, Visual Studio Code 1.68.1

## Summary
The analysis of the election shows: 
- 3,6971,100 votes were cast across 3 counties: Jefferson, Denver, and Arapahoe.
- The candidates were:
    - Charles Casper Stockham 
    - Diana DeGette 
    - Raymon Anthony Doane 

## Results
Each Candidates resultes were as follows:
   - Charles Casper Stockham : 85,213 votes, 23.0% of the total.
   - Diana DeGette : 272,892 votes, 73.8% of the total.
   - Raymon Anthony Doane : 11,606 votes 3.1% of the total.


The winner of the election was: 
   - Diana DeGette with 73.8% of the total votes cast, 272,892.
  
## Challenge
The Pypoll_Challenge.py file is a refactored version of the Pypoll.py script, difference being it calculates the voter turnout in each county aswell. 
  - Jefferson county : 38,855 voters, 11% of the total.
  - Denver county : 306,055 voters, 83% of the total.
  - Arapahoe county : 24,801 voters, 7% of the total.

As is, the code is able to be used to count votes in any election. With a little more refactoring, it would be possible to dig a little more into the data by calculating each candidate's results in each county. This would help determine the general sentiment of each county.


