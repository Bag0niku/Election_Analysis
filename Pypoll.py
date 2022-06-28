import os

# Script Requirements:
# 1) Total number of votes cast
# 2) A complete list of candidates who received votes
# 3) Total number of votes each candidate received
# 4) Percentage of votes each candidate won
# 5) The winner of the election based on popular vote

#  ==================================

# Steps to accomplish Requirements: 

# 1) open data file and retrieve the information: 
data_filepath = os.path.join("Resources", "election_results.csv")
file_to_save =  os.path.join("Analysis", "election_analysis.txt")
# open and import the file
with open(data_filepath, 'r') as file:
    data = file.readlines()
    file.close()

# clean up the data a bit, change the data types from a sting to a list to iterate through and extract information.
for index, row in enumerate(data):
    data[index] = row.split(sep=',')       # Changes the row from a string into a list. at the comma's.
    data[index][2] = data[index][2][:-1]   # Removes the '\n' marker at the end of the candidate names
    
    
# 2) save the list of counties and names voted for
candidates = list()
counties = list()

for row in data[1:]:
    candidates.append(row[2])
    counties.append(row[1])

candidates = set(candidates)   # Removes the duplicates
counties = set(counties)       # Removes the duplicates

# 3) calculate the total number of votes cast in total by county and by name
total_count = len(data) - 1                        # total rows in data minus the header row
county_dict = dict().fromkeys(counties, 0)         # total votes cast in each county
candidate_dict = dict().fromkeys(candidates, 0)    # total votes cast for each candidate
breakdown_dict = dict().fromkeys(candidates, dict().fromkeys(counties, 0))    # breakdowns of votes cast for each candidate in each county

for row in data[1:]: 
        candidate_dict[row[2]] += 1    # counting votes cast for candidate        
        county_dict[row[1]] += 1       # counting votes cast in the county
        breakdown_dict[row[2]][row[1]] += 1    # counting votes cast for candidates in each county

# 5) calculate percentage of votes each name recieved in total and by county
percent_dict = dict() #.fromkeys(candidates, round(((candidate_dict[name]/total_count)*100), 2))
for name in candidate_dict.keys():
    percent_dict[name] = round(((candidate_dict[name]/total_count)*100), 2)


# print(percent_dict)


# 6) determine which name has the most votes and display as the winner
winning_votes = max(candidate_dict.values())

for name in candidate_dict:
    if candidate_dict[name] == winning_votes:
        global winner 
        winner = (name, percent_dict[name])

with open(file_to_save, 'w') as file:
    file.write(f"{winner[0]} is the winner with {winner[1]}% of the votes.")
    file.close()


