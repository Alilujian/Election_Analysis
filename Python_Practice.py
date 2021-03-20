counties = ["Arapahoe", "Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

counties_tuple = ("Arapahoe", "Denver", "Jefferson")

counties_dict ={}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
counties_dict.items()
counties_dict.keys()
counties_dict.values()
counties_dict.get("Denver")

voting_data = []
voting_data.append({"county": "Arapahoe", "registered_voters":422829})
voting_data.append({"county": "Denver", "registered_voters": 463353})
voting_data.append({"county": "Jefferson", "registered_voters": 432438})

print(voting_data)

# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print(f"I received " + str(percentage_votes)+"% of the total votes.")


counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not in the list of counties.")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Araphoe and El paso are in the list of counties.")
else:
    print("Araphoe or El Paso is not in the list of counties.")
if "Arapahoe" in counties or "El Paso" in counties:
    print("Araphoe or El Paso is in the list of counties.")
else:
    print("Araphoe and El Paso are not in the list of counties.")

for county in counties:
    print(county)

for i in range(len(counties)):
    print(counties[i])

for county in counties_dict:
    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))


for county, voters in counties_dict.items():
    print(county + " county has " + str(voters)+ " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

print(message_to_candidate)

# Import the datatime class from the datetime module
import datetime as dt
# Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()
# print the present time
print("The time right now is ", now)