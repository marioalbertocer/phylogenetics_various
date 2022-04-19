import os,sys
from Bio import SeqIO

# para correr esto... python3 path2genome(nucleotides) path2geneFamilies out listadetaxa 
# output va a ser un forlder que contiene dos folders, uno para los archivos con nombres y otro para las familias génicas retrotraducidas

# variables
gp = sys.argv[1] + "/"
gfp = sys.argv[2] + "/"
outdir = sys.argv[3] + "/"
names = outdir + "names/"
gfs_new = outdir + "gfs_new/"
os.system("mkdir " + names)

# haciendo el directorio de nombre de taxa y nombre de archivo con nucleótidos
taxa_list = open(sys.argv[4], "r").readlines()
taxa_list_dir = {}
for i in taxa_list:
	if "_" in i:
		taxa_list_dir[i.split("\t")[0]] = i.split("\t")[1]].strip()

# este loop hace los archivos de nombres
for i in os.listdir(gfp):
	if i.endswith(".fa"):
		gf_names = open(names + i.replace(".fa, ".txt"), "w")
		for rec in  SeqIO.parse(gfp + i, "fasta"):
			gf_names.write("%s\n" % str(rec.id)

# este loop toma los arhivos de nombre creados arriba y retrotraduce las familas génicas
for nfile in os.listdir("names"):
	if nfile.endswith(".txt"):
		gfs_new_file = open(gfs_new + nfile.replace(".txt", ".fa"))
		gf_names = open(names + nfile, "r").readlines()
		for gf_name in gf_names:
			taxa = gf_name[:10]
			for rec in SeqIO.parse(taxa_list_dir[taxa], "fasta")
				if rec.id == gf_name.strip():
					gfs_new_file.write("%s\n%s" % (str(rec.id), str(rec.seq)))
		

