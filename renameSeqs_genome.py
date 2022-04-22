import os,sys
from Bio import SeqIO

# para correr esto.... python3 path2names_list path2genomes(cds) path2out

path2nameslist = sys.argv[1]
path2genomes = sys.argv[2] + "/"
path2out = sys.argv[3] + "/"

if not os.path.exists(path2out):
	os.system("mkdir " + path2out)
else:
	"the output path already exists. Remove the directory and run the script again"
	quit()
	

nameslists_file = open(path2nameslist, "r").readlines()
namesdir = {}
for i in nameslists_file:
	if "_" in i:
		namesdir[i.split("\t")[0]] = i.split("\t")[1].strip()

for genone_file in path2genomes:
	if genome_file.endswith(".fasta"):
		newG = open(path2out + genome_file, "w")
		for rec in SeqIO.parse(genome_file, "fasta"):
			newG.write("%s\n%s\n" % (namesdir[str(rec.id)], str(rec.seq)))
		print("%s\tdone" % genome_file)
