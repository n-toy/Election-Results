import csv
import os


#Path to file 
file_to_load = os.path.join('Resources','election_results.csv')

#vote count var initalize
tot_votes= 0
#Candidate list and dictionary init
candidate_list = []
candidate_votes = {}

#County list and dictionary init
county_list = []
county_votes = {}


with open(file_to_load,'r') as election_data:
    #Read the file into 'file_reader var
    file_reader = csv.reader(election_data)
    #read the header row. We can do this because we're still looking at the first row in file_reader
    headers = next(file_reader)

    for i in file_reader:
    
    #Count the total number of votes
        tot_votes += 1 
    #Candidates section
        #Grab Candidate Name in column 3
        candidate_name = i[2] 
        #Append list of candidates to list if they don't exist
        #Add to dictionary if the candidate does not exist
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # iterate and update the value of the dictionary while we parse through the data
        candidate_votes[candidate_name] += 1
    
    #County Section
        #Grab County Name in Column 2
        county_name = i[1]
        #append list of counties to list if they don't exist
        #Add to dictionary if the county does not exist
        if county_name not in county_list:
            county_list.append(county_name)
            county_votes[county_name] = 0
        #iterate and update the value of the dictionary while we parse through the data
        county_votes[county_name] += 1

election_summary = (
    f"\nElection Results \n"
    f"------------------------------- \n"
    f"Total Votes: {tot_votes:,}\n"
    f"------------------------------- \n"

)

#Moving everything into the election_results file write
with open(os.path.join('analysis','election_results.txt'),"w") as txt_file:
    #Write Election results to file
    txt_file.write(election_summary)
    print(election_summary)

    #------------------------------COUNTY--------------------------------
    #Lets find out what county had the most votes
    #initalize some vars to track who the winnign county is. 
    winning_county = ""
    winning_county_count = 0
    winning_county_percentage = 0

    txt_file.write('\nCounty Votes: \n')
    print('County Votes: \n')
    for county in county_votes:
        #for a given county grab the number of votes they got
        votes_county = county_votes[county]
        #Grab the total # of votes in our data set (row number count)
        votes_all = tot_votes
        #vote County perecentage calc yee yee
        vote_county_percentage = int(votes_county)/int(votes_all)*100

        #determine if current county is the winniner!
        if(votes_county > winning_county_count) and (vote_county_percentage > winning_county_percentage):
            winning_county = county
            winning_county_count = votes_county
            winning_county_percentag = vote_county_percentage

        #format output of da counties
        county_results = (f"{county}: {vote_county_percentage:.1f}% ({votes_county:,})\n")
        txt_file.write(county_results)
        print(county_results)

    winning_county_summary = (
        f"\n------------------------------- \n"
        f"Largest County Turnout: {winning_county}\n"
        f"--------------------------------- \n"
    )


    txt_file.write(winning_county_summary)
    print(winning_county_summary)


    #------------------------------CANDIDATE--------------------------------
    #Lets find out who had the most votes by percentage, and who the winner is!
    #Initalize ssome vars to track who the winning candidate is going to be

    winning_candidate = ""
    winning_candidate_count = 0
    winning_candidate_percentage = 0

    #Initialize some vars to track county with most votes!

    for candidates in candidate_votes:
        #for a given candidate grab the number of votes they got
        votes_candidate = candidate_votes[candidates]
        #Grab the total # of votes in our data set (row number count)
        votes_all = tot_votes
        #Vote percentage calc ayyeeee
        vote_percentage = int(votes_candidate)/int(votes_all) * 100


        #Determine if current candidates is better than current winning candidiate vars.
        #Can do this iterably 
        if (votes_candidate > winning_candidate_count) and(vote_percentage > winning_candidate_percentage):
            winning_candidate = candidates
            winning_candidate_count = votes_candidate
            winning_candidate_percentage = vote_percentage
        #format output of da candidates
        candidate_results = (f"{candidates}: {vote_percentage:.1f}% ({votes_candidate:,}) \n")
        txt_file.write(candidate_results)
        print(candidate_results)

    
    winning_candidate_summary = (
        f"--------------------------------- \n"
        f"Winner: {winning_candidate}\n"
        f"Winner Vote Count: {winning_candidate_count:,}\n"
        f"Winner Vote Percentage: {winning_candidate_percentage:.1f}%\n"
        f"--------------------------------- "
    )
        



    txt_file.write(winning_candidate_summary)
    print(winning_candidate_summary)   
    



