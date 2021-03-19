# Add our dependencise
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)


# Using the open() function with the "w" mode we will write data to the file
# outfile = open(file_to_save, "w")
# Write some data to the file
# outfile.write("Hello World")




# Close the file


# To do: perform analysis


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote


# Close the file
election_data.close()