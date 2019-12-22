#Import modules
import pandas as pd

#Read CSV file

poll_data = "../../../ClassRepo6/UofM-STP-DATA-PT-11-2019-U-C/03-Python/Homework/PyPoll/Resources/election_data.csv"
poll_df = pd.read_csv(poll_data)

#The total number of votes cast

total_votes = len(poll_df.index)

#A complete list of candidates who received votes

candidate_list = poll_df.Candidate.unique()

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.

winner_count = poll_df['Candidate'].value_counts().max()
winner_name = poll_df['Candidate'].value_counts().idxmax()

#Print results

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
print("-------------------------")
print(f"Winner: {winner_name} {winner_count}")
print("-------------------------")

#Export text file