#Import modules
import os
import csv

#Define path to election_data.csv
election_data = os.path.join('.','Resources', 'election_data.csv')

#Open the csv file and pass to csvreader
with open(election_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

#Create a Cadidate list for further data analysis    
    #candidate = []
    #for row in csvreader:
        #candidate.append(row[2])
#Revised to utilize list comprehension
    candidate = [row[2] for row in csvreader]
#Pass total_votes value to variable by using len of list candidate
total_votes = (len(candidate))

#Create a dictionary with unique candidate names and a count of how many occurances
vote_count = {}
for candidate in candidate:
    count = vote_count.get(candidate, 0)
    count += 1
    vote_count[candidate] = count

#Revised to the code below to automate the print output
#for candidate, count in vote_count.items():
    #print(candidate +': ' + str('{:.3f}'.format((count/total_votes)*100)) + '%' + " (" + str(count) + ')')
#Not used after a more efficient print method was developed with a nested for loop
    # Khan_vote = (vote_count['Khan'])
    # Correy_vote = (vote_count['Correy'])
    # Li_vote = (vote_count['Li'])
    # OTooley_vote = (vote_count['O\'Tooley'])
    # Khan_percent = ('{:.3f}'.format((Khan_vote/total_votes)*100))
    # Correy_percent = ('{:.3f}'.format((Correy_vote/total_votes)*100))
    # Li_percent = ('{:.3f}'.format((Li_vote/total_votes)*100))
    # OTooley_percent = ('{:.3f}'.format((OTooley_vote/total_votes)*100))

#Create a text file with the required output
with open("Election_Results.txt", "w") as f:
    print('Election Results', file=f)
    print('---------------------------', file=f)
    print(f'Total Votes: {total_votes}', file=f)
    print('---------------------------', file=f)
    for candidate, count in vote_count.items():
        print(candidate +': ' + str('{:.3f}'.format((count/total_votes)*100)) + '%' + " (" + str(count) + ')', file=f)
    print('---------------------------', file=f)
    print(f'Winner: {max(vote_count, key=vote_count.get)}', file=f)
    print('---------------------------', file=f)

#Print required output to terminal
print('Election Results')
print('---------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------')
for candidate, count in vote_count.items():
    print(candidate +': ' + str('{:.3f}'.format((count/total_votes)*100)) + '%' + " (" + str(count) + ')')
print('---------------------------')
print(f'Winner: {max(vote_count, key=vote_count.get)}')
print('---------------------------')