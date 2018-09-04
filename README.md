# **Cydrasil:** A comprehensive phylogenetic tree of cyanobacterial 16s rRNA gene sequences
Daniel Roush, Ana Giraldo-Silva, Vanessa M. C. Fernandes, Nathali Maria Machado de Lima, Corey Nelson, Sam McClintock, Sergio Velasco Ayuso, Kevin Klicki, Blake Dirks, Watson Arantes, Kira Sorochkina, and Ferran Garcia-Pichel

School of Life Sciences, Arizona State University, 85282 Tempe, Arizona, USA

Center for Fundamental and Applied Microbiomics, Biodesign Institute, Arizona State University, 85282 Tempe, Arizona, USA

## **Methods**
This is a phylogenetic tree containing 980 cyanobacterial sequences, downloaded from NCBI and used for placement of sequence variants (sOTUs) from 16s rRNA gene amplicon studies. 
The reference alignment was generated using SSUALIGN<sup>1</sup> with default parameters and then masked using SSUMASK with the automatically computed alignment confidence values (posterior probabilities). A maximum-likelihood phylogenetic tree was then generated using the RAxML-HPC2<sup>2</sup> Workflow on XSEDE (8.2.9) on the CIPRES Science Gateway<sup>3</sup>. The ML + thorough bootstrap workflow was used with the following modified parameters: 1000 bootstraps (-N 1000) and the GTRGAMMA model. All other parameters were left at default values.  

## **Use**
A FASTA file containing sequences of interest (typically the reference sequence file from Qiime1/2) is aligned to the reference alignment using an alignment tool. We use PaPaRa<sup>4</sup> alignment and the repository contains a phylip (.phy) alignment to use with PaPaRa. 
```
papara -t cydrasil-rc1-bipartitions-tree-1000.nwk -s cydrasil-rc1-alignment-phylip.phy -q ref-seqs.fasta -n combined-aln
```
The output combined alignment is then used as the input into the Evolutionary Placement Algorithm function of RAxML 8. 
```
raxml-HPC ¬-f v ¬-s papara_alignment.combined-aln -¬t cydrasil-rc1-bipartitions-tree-1000.nwk -¬m GTRGAMMA -¬n SeqPlacements 
```
To visualize the new phylogenetic tree containing the sequences of interest, the placement file (_RAxML_portableTree.SeqPlacements.jplace_) is uploaded onto [iTOL] (https://itol.embl.de/)<sup>5</sup>. Placements are a dataset within iTOL and can be toggled. Nodes with sequences of interest are visualized with red spheres and clicking a node will show a breakdown of sequence ids and the corresponding confidence values for that node. 

## **References**
1. 	Nawrocki E. 2009. Structural RNA Homology Search and Alignment Using Covariance Models. Washington University School of Medicine.
2. 	Stamatakis A. 2014. RAxML version 8: A tool for phylogenetic analysis and post-analysis of large phylogenies. Bioinformatics 30:1312–1313.
3. 	Miller MA, Pfeiffer W, Schwartz T. 2010. Creating the CIPRES Science Gateway for inference of large phylogenetic trees. 2010 Gatew Comput Environ Work GCE 2010.
4. 	Berger SA, Stamatakis A. 2011. Aligning short reads to reference alignments and trees. Bioinformatics 27:2068–2075.
5. 	Letunic I, Bork P. 2016. Interactive tree of life (iTOL) v3: an online tool for the display and annotation of phylogenetic and other trees. Nucleic Acids Res 44:W242–W245.
