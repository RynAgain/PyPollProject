#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#headers inclued Ballot_ID, County, Candidate

#imports
import os 
import csv
import time

file_to_load = "Resources/election_results.csv"
election_data = open(file_to_load, "r")
#perform analysis then close
with open(file_to_load) as election_data:
    print(election_data)
election_data.close()

#FUNCTIONS

#open the data file


#main code block