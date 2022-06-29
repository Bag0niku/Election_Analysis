from distutils import text_file
import os


#filepaths needed for data retrieval and saving information.
data_filepath = os.path.join("Resources", "election_results.csv")
file_to_save =  os.path.join("Analysis", "election_analysis.txt")

# open and import the data
with open(data_filepath, 'r') as file:
    data = file.readlines()
    file.close()

# clean up the data a bit, change the data types from a sting to a list to iterate through and extract information.
for index, row in enumerate(data):
    data[index] = row.split(sep=',')       # Changes the row from a string into a list at the comma's.
    data[index][2] = data[index][2][:-1]   # Removes the '\n' marker at the end of the candidate names
    
# save the list of counties and names candidates for
total_count = len(data) - 1     # total rows in data minus the header row = total votes
candidates = dict()             # for holding the candidate names and their total vote count
counties = dict()               # for holding the county names and their total voter turnout


# 3) calculate the number of votes for each candidate cast for a candidate or in a county
for row in data[1:]:
    county = row[1]
    name = row[2]
    if county not in counties.keys():
        counties[county] = 1
    else:
        counties[county] += 1
     
    if name not in candidates.keys():
        candidates[name] = 1
    else:
        candidates[name] += 1
    

# find voter turnout percentage and the county with the highest turnout.
voter_turnout = dict().fromkeys(counties.keys(), 0)
winning_votes = max(counties.values())

for place in counties.keys():
    voter_turnout[place] = round((counties[place]/total_count)*100)
    if counties[place] == winning_votes:
        global winning_county
        winning_county = (place, voter_turnout[place])

# find the winner
winning_votes = max(candidates.values())
for name in candidates.keys():
    if candidates[name] == winning_votes:
        global winner 
        winner = (name, round(((candidates[name]/total_count)*100), 1))

text_file_header = (
    f"Election Results:\n"
    f"-------------------------\n"
    f"Total Votes : {total_count:,}\n"
    f"-------------------------\n")


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winner[0]}\n"
    f"Winning Candidate's Count: {candidates[winner[0]]:,}\n"
    f"Winning Percentage: {winner[1]:}%\n"
    f"-------------------------\n"  )


# Output the information learned to a text file (file.write) and the terminal (print).
with open(file_to_save, 'w') as file:
    print(f"-------------------------\n")
    print(text_file_header)
    file.write(text_file_header)
    
    # each county's voter turnout information
    print(f"Voter Turnout: \n")
    file.write(f"Voter Turnout: \n")
    for place in counties.keys():
        print(f"{place} county : {counties[place]:,} voters, {voter_turnout[place]}% of the total.\n")
        file.write(f"{place} county : {counties[place]:,} voters, {voter_turnout[place]}% of the total.\n")

    file.write(f"-------------------------\n")
    print(f"-------------------------\n")
    print(f"Largest County Turnout: {winning_county[0]}\n")
    file.write(f"Largest County Turnout: {winning_county[0]}\n")
    file.write(f"-------------------------\n")
    print(f"-------------------------\n")
    
    # each candidate's results.
    print(f"Candidate Information: \n")
    file.write(f"Candidate Information: \n")
    for name in candidates.keys():
        print(f"{name} : {candidates[name]:,} votes,  {round(((candidates[name]/total_count)*100), 1)}% of the total.\n")
        file.write(f"{name} : {candidates[name]:,} votes, {round(((candidates[name]/total_count)*100), 1)}% of the total.\n")

    # the winner's information.
    print(winning_candidate_summary)
    file.write(winning_candidate_summary)
    

    file.close()
    
