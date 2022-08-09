import os,sys
from Bio import SeqIO

# Código para crear intérvalos de 100 de cada chr y evaluar su GC content

print("%s\t%s\t%s\t%s\t%s" % ("Chr", "Start", "End", "Lenght", "Sequence"))

for cs in SeqIO.parse("test_genome.fasta", "fasta"):
	id_s = str(cs.id)
	se_s = str(cs.seq)
#	print(se_s)
	c = 0
	inter = (len(se_s)-9)
	gcs = []
	inters = []
	int_dict = {}
	conc = "n"
	candCentromer = ""
	
	# Definir intervalos de a 10 avanzando de a 1 nucleótido
	for i in range(0,int(inter)):
		int_s = se_s[c : c+10]
		c = c+1
		# print(int_s)
		
		#GC and AT content
		gc_c = 0
		at_c = 0
		
		for n in int_s:
			if n == "C": gc_c += 1
			if n == "G": gc_c += 1
			if n == "A": at_c += 1
			if n == "T": at_c += 1
		gc_cp = (gc_c/10)*100
		gcs.append(int(gc_cp))
		int_dict[int_s] = int(gc_cp)
# 		print(int_dict.items())
		
		#Intervalos con gc_cp (GC content) igual o mayor a 90%
		
		if gc_cp >= 90: 
			if conc != "y": lf = i
			conc = "y"
		else: 
			if candCentromer != "" :
				conc = "s"
			else:
				conc = "n"
		
		while conc == "y": candCentromer += int_s[0] # Formar seq con el nctd inicial de los intervalo
		if conc == "s":
			if len(candCentromer) > 5:
				candCentromer += int_s[1:-1]
				ll = i + 9
				int_dict[str(lf) + "_" + str(ll)] = candCentromer
			candCentromer = ""
   
   biggest_locus = sorted(d, key=lambda k: len(d[k]), reverse=True)[0]
   biggest_seq = int_dict[biggest_locus]
   
# 	   
# 			#Definir secuencia centromérica
# 			if start_cent in se_s:
# 				lenght_start = len(start_cent)
# 				n_start = int(se_s.find(start_cent)) #Nctd inicial del centrómero
# 				lenght_cent = int(lenght_start) + 9 #Longitud del centrómero
# 				n_end = n_start + (lenght_cent) #Nctd final del centrómero
# 				seq_cent = str(se_s[n_start:n_end]) #Secuencia centrómero
# 	
# 	print("%s\t%s\t%s\t%s\t%s" % (id_s, n_start, n_end, lenght_cent, seq_cent))
# 			
# 			print("%s, %s, %s, %s, %s" % (id_s, int_s, int_s[0], int_s[9], int(gc_cp)))		
# 		print("%s, %s" % (int_s, int(gc_cp)))
# 	print("%s, %s" % (id_s, str(gcs)))
            