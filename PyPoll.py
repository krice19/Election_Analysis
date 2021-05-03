# steps 
import csv

#blocking the below out so we do it the import OS way
'''
#path to CSV file is:
#Resources/election_results.csv

file_to_load = "Resources/election_results.csv"

#tells us that the csv file is in the resources  folder

#next, we need to open the file to load

election_data = open(file_to_load, "r")

#can do this instead of above 
with open(file_to_load) as election_data:
    print(election_data)
'''

#using OS way

#add dependecy
import os
#assign variable to load the file from a path
file_to_load = os.path.join("Resources","election_results.csv")
#assign variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

total_votes = 0
candidate_options = []
candidate_votes = {}

winning_candidate = " "
winning_count = 0
winning_percentage = 0



#open the election results and read the file
with open(file_to_load) as election_data:
    # read and analyze the data
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    
    for row in file_reader:
        #add to total vote count
        total_votes += 1
        #print candidate name from each row
        candidate_name = row[2]
        #if staement to check if name not already in list

        if candidate_name not in candidate_options:
            #add candidate name to the list
            candidate_options.append(candidate_name)
            #begin tracking candidates vote count
            candidate_votes[candidate_name] = 0

        #add a vote to the candidates vote count - needs to be out of if statement
        candidate_votes[candidate_name] += 1
    
    #gives us total votes without the header included
    #with header it would be 369712
    print(total_votes)
    print(candidate_options)
    print(candidate_votes)

    #itreate through candidate list
    for candidate_name in candidate_votes:
        #get vote count of the candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        #print candidate name and percentage of votes
        print(f"{candidate_name}: receiveed {vote_percentage:.2f}% of the vote.")
        
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #sets votes and percentage equal to winning count/percetnage as we loop through each candidate name
            winning_count = votes
            winning_percentage = vote_percentage
            #sets winning candidate to candidate name in for loop
            winning_candidate = candidate_name
            
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
    
    
   

    

#1. The total number of votes cast
#2. Complete list of candidates who recieved votes
#3. Percentage of votes each  candidate won
#4. The total number of votes each candidate won
#5. Winner of the election based on popular vote