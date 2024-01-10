# Building a head-to-head table

My solution first converts a given json file into a dictionary with the `json` library.
Then, I retrieve the keys of the dict as a list `teams` (which holds the names of each of the teams). 
I append a buffer and use the length of the list to construct an empty table (as a 2D array).

Then, using the same list, I fill in the labels of the table in the first for loop.
The second for loop traverses the created table and fills out each row with the win data from the given json. 
This is done by iterating through each team, skipping if the team's value to fill out is itself, which there could not be data for.
The function returns the table after each row has been traversed.

The last line in the file runs the function on the provided sample data in `example.json`.