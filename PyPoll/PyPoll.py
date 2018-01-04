import os
import csv

polling_csv = os.path.join("election_data_1.csv")
Election_Data = []
voters = []
candidates = []
candidate_list = []
Vestal = 0
Torres = 0
Seth = 0
Cordin = 0

with open(polling_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    next(csv_reader, None)
    for row in csv_reader:
        voters.append(row[0])
        candidates.append(row[2])
        total_votes = len(voters)
    for i in candidates:
        if i not in candidate_list:
            candidate_list.append(i)
        elif i == 'Vestal':
            Vestal = Vestal + 1
        elif i == 'Seth':
            Seth = Seth + 1
        elif i == 'Torres':
            Torres = Torres + 1
        elif i == 'Cordin':
            Cordin = Cordin + 1
        
    Vestal_perc = Vestal/total_votes
    Torres_perc = Torres/total_votes
    Seth_perc = Seth/total_votes
    Cordin_perc = Cordin/total_votes

Election_Data = [Vestal, Seth, Torres, Cordin]
Election_percentages = [Cordin_perc, Seth_perc, Torres_perc, Vestal_perc]
Winner = max(Election_Data)

print("Election Results")
print("-------------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------------")
print("Vestal: " +str(round(Vestal_perc*100, 0)) + "% " + "(" + str(Vestal) + ")")
print("Torres: " +str(round(Torres_perc*100, 0)) + "% " + "(" + str(Torres) + ")")
print("Seth: " +str(round(Seth_perc*100, 0)) + "% " + "(" + str(Seth) + ")")
print("Cordin: " +str(round(Cordin_perc*100, 0)) + "% " + "(" + str(Cordin) + ")")
print("-------------------------------")
print("Winner: " + str(candidate_list[Election_Data.index(max(Election_Data))]))
print("-------------------------------")



PyPoll = os.path.join("PyPoll.csv")
with open(PyPoll, 'w', newline="") as datafile:
    csvWriter = csv.writer(datafile)
    csvWriter.writerow(["Election Results"])
    csvWriter.writerow(["-------------------------------"])
    csvWriter.writerow(["Total Votes: " + str(total_votes)])
    csvWriter.writerow(["-------------------------------"])
    csvWriter.writerow(["Cordin: " +str(round(Cordin_perc*100, 0)) + "% " + "(" + str(Cordin) + ")"])
    csvWriter.writerow(["Seth: " +str(round(Seth_perc*100, 0)) + "% " + "(" + str(Seth) + ")"])
    csvWriter.writerow(["Torres: " +str(round(Torres_perc*100, 0)) + "% " + "(" + str(Torres) + ")"])
    csvWriter.writerow(["Vestal: " +str(round(Vestal_perc*100, 0)) + "% " + "(" + str(Vestal) + ")"])
    csvWriter.writerow(["-------------------------------"])
    csvWriter.writerow(["Winner: "+ str(candidate_list[Election_Data.index(max(Election_Data))])])
    csvWriter.writerow(["-------------------------------"])