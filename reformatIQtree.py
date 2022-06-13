import os, sys
import dendropy

# This script takes the output .treefile from IQ-tree that you generate in IQ-tree as...
# iqtree2 -s alignment -B 1000 -alrt 1000 
# and combines the information in just one tree that is compatible with figTree.
# use as ... python3 path_to_lengths_tree(nexus) path_to_bootstrap_tree(nexus) path_to_output(folder)
if len(sys.argv) == 3:
	tree = (open(sys.argv[1], "r").readlines())[0]
	tree_object = dendropy.Tree.get_from_string(tree, schema="newick")
	for nd in tree_object:
		if type(nd.label) is str:
			if "/" in nd.label:
				if sys.argv[2] == 'bt' : nd.label = ((nd.label).split("/")[1]).strip()
				if sys.argv[2] == 'sa' : nd.label = ((nd.label).split("/")[0]).strip()		
	tree_mod = (tree_object.as_string(schema="newick",)).strip()			
	print(tree_mod)
else:
	print("""
		This script takes the output .treefile from IQ-tree that you generate as...
		iqtree2 -s alignment -B 1000 -alrt 1000
		and produces a simpler version of the tree that is compatible with FigTree and
		that only contains either bootstrap support OR SH-aLRT (you choose)
		Note: if you just added bootstrapping OR SH-aLRT but not both at the same time, 
		then you don't need this script.
		
		use as ... python3 reformatIQtree.py path_to_tree node_support
		
		* path_to_tree: Path to the tree (.treefile extension)
		* node_support: Node support type (bootstrap or SH-aLRT) for the output tree.	
						bt: bootstrap
						sa: SH-aLRT		  
		""")