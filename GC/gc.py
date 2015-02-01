# Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).
# Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

file=open('test input.txt','r')

id=[]
gcp=[]

for line in file:
	if line[0]=='>':
		pass
		print line[10:14:1]
		tid=line[10:14:]
		id.append(tid)
	else :
		pass
		sum_gc=line.count("G")+line.count("C")
		gcp.append((float(sum_gc)*100)/len(line))

print "Rosalind_"+id[gcp.index(max(gcp))]
print max(gcp)