# PyPollProject

## Project Overview 
The Board of Elections in Colorado has asked us to conduct an audit of the recent local congressional election, and has provided us a CSV file to analyze.  Our goal is to create a script that can be reused, to do the following tasks:  

1. Calculate the total number of votes casts. 
2. Get a complete lists of candidates who received votes. 
3. Get the lists of counties in the election. 
4. Calculate the percentage of votes for each candidate won.
5. Calculate the percentage of votes for each county.

# Resources
- Data Sources:  election_results.csv
- Code Output:  election_analysis.txt

## Summary
- In this election 369,711 votes were recorded for three candidates:  
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anothony Doane

- The voting data was organized into three counties:
    - Jefferson County
    - Denver County 
    - Arapahoe County


## Results
- Denver county had the largest voter turnout with 306,055 votes (82.8%).  Figure below shows the outcome between the three.
(insert picture here)

Here are the county results written in plain text:
    - Jefferson: 38,855 votes (10.5%)
    - Denver 306,055 votes (82.8%)
    - Arapahoe 24,801 (6.7%)


- Diana DeGette had the largest number of votes at 272,892 (73.8%).  Figure below shows a breakdown of the votes by candidate.
(insert picture here)

Here are the candidate results written in plain text:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)

The winner of the election was:
    - Diana DeGette with 272,892 votes (73.8%)
(insert picture here)

# Audit Summary 
The code should be already prepared to be reused.  All you'd have to do is provide a new csv file of results with the same data structure as the original.  Then just update the path of the results file to the new one.  If you wanted to get real fancy about it you could rewrite the code to except an input as the path.  If you wanted to get really really fancy you could use the tkinter module to create a GUI interface that would make it even easier to input a path name. 

The main goal of providing a new data set is to update teh Candidate names and county names inside the code, this will update all the outputs that are written to the terminal.

To further insure that the audit is useful it would be good to check for duplicate ballot IDs so that votes aren't counted twice for some reason.
