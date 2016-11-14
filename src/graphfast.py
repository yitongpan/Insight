import re
import graph as grp

graph = grp.Graph()
pat = '.*,' * 4
fn_pat = 'txt$'

while True:
	depth = input("Which degree of friends you want to cover? 1,2 or 4\n")
	if depth not in ['1', '2', '4']:
		print("Your input for degree of friedns is not valid")
		continue
	else:
		depth = int(depth)
		break

while True:
	fn = input("what is the file name for your output? (ending in .txt)\n")
	if not re.search(fn_pat, fn):
		print("Your output filename is not .txt file")
		continue
	else:
		break

with open('batch_payment.txt', 'r') as infile:
	firstline = infile.readline()
	for line in infile:
		if re.search(pat, line):
			line = line.split(',')
			id1 = line[1]
			id2 = line[2]
			graph.insertEdge(id1, id2)

with open('stream_payment.txt','r') as infile, open(fn,'w') as outfile:
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
