import os, sys
from Bio import GenBank
from Bio import SeqIO

sequences_paths = list(map(lambda x: x.strip(), open(sys.argv[1])))
outdir = sys.argv[2] + "/output/"
if not os.path.exists(outdir) : os.system("mkdir " + outdir)
concatenated = open(outdir + "concatenated.fasta", "w")
supermatrix = {}

# setting the names of the concatenated file
for rec in SeqIO.parse(sequences_paths[0], "fasta"): supermatrix[str(rec.id).split("_")[0]] = ""

# populating the concatenated file with the sequences per file
for alm in sequences_paths:
	len_seq = []
	print(alm)
	for rec in SeqIO.parse(alm, "fasta"):
		name_seq = str(rec.id).split("_")[0]# if "_" in rec.id else str(rec.id)
		if len(str(rec.seq)) not in len_seq: len_seq.append(len(str(rec.seq)))
		supermatrix[name_seq] += str(rec.seq)
		
	if len(len_seq) != 1 :
		print("wrong format in file %s " % alm)
		quit()
		
for n, s in supermatrix.items(): concatenated.write(">%s\n%s\n" % (n, s))	
			
		
		

