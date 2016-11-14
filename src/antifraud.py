import re
import graph as grp
from os import path

graph = grp.Graph()
pat = '.*,' * 4
fn_pat = 'txt$'

# For the path of input
script_dir = path.dirname(__file__)
input_batch = path.join(script_dir, "../paymo_input/batch_payment.txt")
input_stream = path.join(script_dir, "../paymo_input/stream_payment.txt")

## Ask the user to select the right degree of friends
while True:
	depth = input("Which degree of friends you want to cover? 1,2 or 4\n")
	if depth not in ['1', '2', '4']:
		print("Your input for degree of friedns is not valid")
		continue
	else:
		depth = int(depth)
		break

## For the path of the output
if depth == 1:
	output = path.join(script_dir, "../paymo_output/output1.txt")
elif depth == 2:
	output = path.join(script_dir, "../paymo_output/output2.txt")
else:
	output = path.join(script_dir, "../paymo_output/output3.txt")

# Read in all the data from batch_payment and create an initial graph
with open('input_batch', 'r') as infile:
	firstline = infile.readline()
	for line in infile:
		if re.search(pat, line):
			line = line.split(',')
			id1 = line[1]
			id2 = line[2]
			graph.insertEdge(id1, id2)

# Write the file with the degree we deserved 
with open('input_stream','r') as infile, open(output,'w') as outfile:
	firstline = infile.readline()
	for line in infile:
		if re.search(pat, line):
			line = line.split(',')
			id1 = line[1]
			id2 = line[2]
			if graph.hasPath(id1,id2,depth):
				outfile.write('trusted\n')
			else:
				outfile.write('unverified\n')
			graph.insertEdge(id1, id2)
