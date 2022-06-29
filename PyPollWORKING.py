#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular vote. 


#Add our dependencies
import csv
import os

#assign a variable to load  a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initialize a total vote counter.
total_votes = 0

#Candidate options
candidate_options = []

#1. Declare the empty dictionary.
candidates_votes = {}

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
       
    #Read the header row
    headers = next(file_reader)
   
    #Print each row in the CSV file
    for row in file_reader:
        #Add the total vote count.
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote cocunt
            candidates_votes[candidate_name] = 0

        #Add a vote to that candidate's count
        candidates_votes[candidate_name] += 1

#Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Determine the percneage of votes for each candidate by loopingt through the counts
#Iterate through the candidate list
for candidate_name in candidates_votes:
    # Retrieve vote count of a candidate.
    votes = candidates_votes[candidate_name]

    #Save the results in our text file.
    with open(file_to_save, "w") as txt_file:

        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #to do: print out each candidate's name, vote coutn, and percentage of votes to the terminal

        #determine winning vote count and candidate
        #determine if the votes is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #If true then set winning_count = votes and winning percent = vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            #And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

        #to do: Print out each candidate's name, vote count, and  and percentage of votes to the terminal.
        #print(f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n ")



    winning_candidate_summary = (
        f"--------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"--------------------------\n"
    )
    #print(winning_candidate_summary)

    #Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"--------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"--------------------------\n")
    print(election_results, end="")
    #Save the final vote count to the text file.

    candidate_results = (f"{candidate_name}:  {vote_percentage:.1f}% ({votes:,})\n ")
#Save the candidate results to our text file.


txt_file.write(election_results)






   
  





