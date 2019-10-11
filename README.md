# **Cydrasil 1.5:** A comprehensive phylogenetic tree of cyanobacterial 16S rRNA gene sequences
[![DOI](https://zenodo.org/badge/144063861.svg)](https://zenodo.org/badge/latestdoi/144063861)

Daniel Roush, Ana Giraldo-Silva, Vanessa M. C. Fernandes, Nathali Maria Machado de Lima, Corey Nelson, Sam McClintock, Sergio Velasco Ayuso, Kevin Klicki, Blake Dirks, Watson Arantes, Kira Sorochkina, and Ferran Garcia-Pichel

<sup>1</sup>School of Life Sciences, Arizona State University, 85282 Tempe, Arizona, USA

<sup>2</sup>Center for Fundamental and Applied Microbiomics, Biodesign Institute, Arizona State University, 85282 Tempe, Arizona, USA

## **Interactive Reference Tree**

[Link to Cydrasil v1.5 on iTOL](https://itol.embl.de/shared/fgpcydrasil)

***

## **Methods**
Cydrasil is a sequence database, alignment, and phylogenetic tree containing 1494 cyanobacterial 16S rRNA gene sequences, downloaded from NCBI and IMG and used for placement of sequence variants (sOTUs) from 16S rRNA gene amplicon studies. 
The reference alignment was generated using SSUALIGN<sup>1</sup> with default parameters. This aligner uses a profile-based alignment strategy, in which each target sequence is aligned independently to a covariance model that uses the 16S rRNA gene secondary structure, and then masked using SSUMASK with the automatically computed alignment confidence values (posterior probabilities). A maximum-likelihood phylogenetic tree was then generated using the RAxML-HPC2<sup>2</sup> Workflow on XSEDE (8.2.12) on the CIPRES Science Gateway<sup>3</sup>. The ML + thorough bootstrap workflow was used with the following modified parameters: 1000 bootstraps (-N 1000) and the GTRGAMMA model. All other parameters were left at default values.  

***

## **Use**

### **Step 1**
#### **Alignment of query sequences to reference alignment** 
**There are issues with compiling PaPaRa on new Macs. We will be moving from PaPaRa in Mid-October 2019**

A FASTA file containing sequences of interest (typically the reference sequence file from Qiime1/2) is aligned to the reference alignment. We use PaPaRa<sup>4</sup> alignment and the repository contains a phylip (.phy) alignment to use with PaPaRa. 
[PaPaRa Installation](https://cme.h-its.org/exelixis/web/software/papara/index.html) [PaPaRa Github](https://github.com/sim82/papara_nt)

**Input**

**PaPaRa Arguments**

-t, Reference tree

-s, Reference alignment in phylip (.phy) format

-q, Fasta file containing sequences to be aligned to the reference alignment

-n, Name of output alignment

**Example**
```
papara -t cydrasil-rc1-bipartitions-tree-1000.nwk -s cydrasil-rc1-alignment-phylip.phy 
-q ref-seqs.fasta -n combined-aln
```
The output combined alignment (from step 1) is then used as input (argument -s) for RaxML8 evolutionary placement algorithm.

### **Step 2**

**Input**
**RAxML Arguments**

--f, Mode selection of RAxML (_v_)

--T, Number of threads for multithreading

--t, Reference tree file name (_cydrasil-rc1-bipartitions-tree-1000.nwk_)

--s, Combined alignment from PaPaRa (_combined-aln_)

--m, Substitution model (_GTRGAMMA_)

--n, Name for output

**Output**

Phylogenetic tree with placements in .jplace format (_RAxML_portableTree.SeqPlacements.jplace_)

**Example**
```
raxml-HPC --f v --s papara_alignment.combined-aln --t cydrasil-rc1-bipartitions-tree-1000.nwk 
--m GTRGAMMA --n SeqPlacements 
```

### **Step 3**

**Tree Visualization**

To visualize the new phylogenetic tree containing the sequences of interest, the placement file (_RAxML_portableTree.SeqPlacements.jplace_) is uploaded onto [iTOL] (https://itol.embl.de/)<sup>5</sup>. Placements act as a dataset within iTOL and can be toggled. Nodes with sequences of interest are visualized with red spheres and clicking a node will show a breakdown of sequence ids and the corresponding confidence values for that node. 

Steps to visualize tree in iTOL:

1. Create an user account in the iTOL server

2. Drag .jplace file into an iTOL project

3. Root the tree: Right click on node **I1884** and click re-root tree here

4. From the Controls box set parameters as follows:

>Basic
>- Display mode: Normal
>- Parameters: 0 degree rotation
>- Invert: No
>- Slanted: No
>- Branch lengths: Use
>- Labels: At tips **NOTE:** You can toggle labels to off if the tree slows your computer.
>- Label rotation: On
>- Label alignment: Left

>ADVANCED: No changes. If you are having trouble reading your results, you can use the scaling factors to separate leaves.

>DATASETS
>- Turn on phylogenetic placements 
>- Use “Show query form” to search placement of individiual query sequences
>- Insert query sequence ID and use the “highlight option” to display red spheres indicating phylogenic placement of a given query sequence.

***

## **References**
1. 	Nawrocki E. 2009. Structural RNA Homology Search and Alignment Using Covariance Models. Washington University School of Medicine.
2. 	Stamatakis A. 2014. RAxML version 8: A tool for phylogenetic analysis and post-analysis of large phylogenies. Bioinformatics 30:1312–1313.
3. 	Miller MA, Pfeiffer W, Schwartz T. 2010. Creating the CIPRES Science Gateway for inference of large phylogenetic trees. 2010 Gatew Comput Environ Work GCE 2010.
4. 	Berger SA, Stamatakis A. 2011. Aligning short reads to reference alignments and trees. Bioinformatics 27:2068–2075.
5. 	Letunic I, Bork P. 2016. Interactive tree of life (iTOL) v3: an online tool for the display and annotation of phylogenetic and other trees. Nucleic Acids Res 44:W242–W245.
