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
    
# save the list of counties and names voted for
total_count = len(data) - 1           # total rows in data minus the header row = total votes
candidates = list()
counties = list()
votes = dict()

# 3) calculate the total number of votes cast
for row in data[1:]:
    county = row[1]
    name = row[2]
    if county not in counties:
        counties.append(county)
    else: 
        pass
    if name not in candidates:
        candidates.append(name)
    else:
        pass
    try:
        votes[name] += 1
    except KeyError:
        votes[name] = 1

# find the winner
winning_votes = max(votes.values())

for name in votes.keys():
    print(f"{name} : {round((votes[name]/(len(data)-1)*100), 1)}% ({votes[name]})")

    if votes[name] == winning_votes:
        global winner 
        winner = (name, round((votes[name]/(len(data)-1)*100), 1))


winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winner[0]}\n"
    f"Winning Vote Count: {votes[winner[0]]}\n"
    f"Winning Percentage: {winner[1]}%\n"
    f"-------------------------\n"  )

print(winning_candidate_summary)


