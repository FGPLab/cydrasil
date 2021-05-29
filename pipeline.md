#Pipeline for Generating Phylogeny

## Alignment with SSU-Align

`ssu-prep -x cydrasil-v3-sequence-list.fasta cydrasil-3-ssu-align 6`

`bash cydrasil-3-ssu-align.ssu-align.sh`

`ssu-mask cycydrasil-3-ssu-align`

```
from Bio import AlignIO

input_handle = open("alignment-work\cydrasil-3-ssu-align\cydrasil-3-ssu-align.bacteria.mask.stk", "rU")
output_handle_fa = open("Cydrasil-v3-aln-mask.afa", "w")
output_handle_rel-phy = open("Cydrasil-v3-aln-mask.phy", "w")

alignments = AlignIO.parse(input_handle, "stockholm")
AlignIO.write(alignments, output_handle_fa, "fasta")
AlignIO.write(alignments, output_handle_rel-phy, "phylip-relaxed")

output_handle_fa.close()
output_handle_rel-phy.close()
input_handle.close()

```