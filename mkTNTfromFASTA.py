import os, sys
from Bio import SeqIO

f = sys.argv[1]
n = open(sys.argv[2], "w")

aliLength = 0
ntaxa = 0

for rec in SeqIO.parse(sys.argv[1], "fasta"):
	if aliLength == 0:
		aliLength = len(rec.seq)
	ntaxa += 1

n.write("xread\n")
n.write("%s %s\n" % (aliLength, ntaxa))

for rec in SeqIO.parse(sys.argv[1], "fasta"):
	print(rec.id)
	n.write("%s %s\n" % (rec.id, rec.seq))

n.write(";")
