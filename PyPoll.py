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

#open the election results and read the file
with open(file_to_load) as election_data:
    # read and analyze the data
    file_reader = csv.reader(election_data)

    #read and print the header row
    headers = next(file_reader)
    print(headers)
    

#1. The total number of votes cast
#2. Complete list of candidates who recieved votes
#3. Percentage of votes each  candidate won
#4. The total number of votes each candidate won
#5. Winner of the election based on popular vote