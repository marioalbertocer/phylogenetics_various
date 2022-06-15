import os, sys
from Bio import AlignIO

path2dir =  "/Users/marioceron/codon_alignments_chromo/"

for aliFile in os.listdir(path2dir):
	if aliFile.endswith(".fas"):
		align = AlignIO.read(open(path2dir + aliFile), "fasta")
		distances = {}
		for rec in align:
			seq1 = rec.seq
			distances_i = []
			for rec2 in align:
				seq2 = rec2.seq
				if not rec.id == rec2.id:
					n = 0
					nd = 0
					p = 0
					for site_idx in range(0, len(seq1)):
						if not "-" in [seq1[site_idx], seq2[site_idx]]:
							n += 1
							if seq1[site_idx] != seq2[site_idx]:
								nd += 1 
					p = nd/n
					distances_i.append(p)
			distances[rec.id] = distances_i


		av_distances  = {}
		for key, value in distances.items(): av_distances[key] = (sum(value))/float(len(value))
		print("%s,%s" % (aliFile, ((sum(av_distances.values()))/float(len(av_distances)))))
		
		