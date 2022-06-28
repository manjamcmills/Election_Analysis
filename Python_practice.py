counties = ["Arapahoe", "Denver", "Jefferson"]
if "El Paso" in counties:
        print("El Paso is in the list of counties")
else:
        print("El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
        print("Arapahoe or El Paso is in the list of counties")
else:
        print("Arapohoe and El Paso is not in the list of counties")


for i in range(len(counties)):
        print(counties[i])

counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

for county in counties_dict:
        print(county)



for county in counties_dict.keys():
        print(county)



for voters in counties_dict.values():
        print(voters)


for key, value in counties_dict.items():
        print(county, voters)




#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))
#message_to_candidate = (                
        #f"You received {candidate_votes} number of votes. "
        #f"The total number of votes in the election was {total_votes}. "
        #f"You recieved {candidate_votes / total_votes*100:.3f}% of the total votes. ")

#print(message_to_candidate)

counties_dict = {'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
counties_dict.keys()