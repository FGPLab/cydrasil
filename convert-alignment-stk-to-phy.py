from Bio import AlignIO

input_handle = open("alignment-work/cydrasil-3-ssu-align/cydrasil-3-ssu-align.bacteria.mask.stk", "rU")
output_handle_phy = open("Cydrasil-v3-aln-mask.phy", "w")

alignments = AlignIO.parse(input_handle, "stockholm")
AlignIO.write(alignments, output_handle_phy, "phylip-relaxed")

output_handle_phy.close()
input_handle.close()