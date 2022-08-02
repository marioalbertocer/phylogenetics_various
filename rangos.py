import os,sys
from Bio import SeqIO

r = open("100mers_out.txt", "w")
r2 = open("1000mers_out.txt", "w")

for cs in SeqIO.parse("loco.fasta", "fasta"):
	id_s = str(cs.id)
	se_s = str(cs.seq)
#	print(se_s)
	c = 0
	inter = len(se_s)/1000
	gcs = []
	for i in range(0,int(inter)):
		int_s = se_s[c : c+1000]
		c = c+1000
#		print(int_s)
		gc_c = 0
		at_c = 0
		for n in int_s:
			if n == "C": gc_c += 1
			if n == "G": gc_c += 1
			if n == "A": at_c += 1
			if n == "T": at_c += 1
		gc_cp = (gc_c/at_c)*100
		gcs.append(int(gc_cp))
	print("%s, %s" % (id_s, str(gcs)))
            