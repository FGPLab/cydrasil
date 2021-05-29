from Bio import AlignIO

input_handle = open("alignment-work/cydrasil-3-ssu-align/cydrasil-3-ssu-align.bacteria.mask.stk", "rU")
output_handle_fa = open("Cydrasil-v3-aln-mask.afa", "w")

alignments = AlignIO.parse(input_handle, "stockholm")
AlignIO.write(alignments, output_handle_fa, "fasta")

output_handle_fa.close()
input_handle.close()