
<img src="https://cydrasil-asset-hosting.s3-us-west-2.amazonaws.com/images/cydrasil-v-3-logo.png" alt="Cydrasil Logo" width="800"/>

# A curated cyanobacterial 16S rRNA gene reference package for sequence placement and *de novo* phylogenetic analysis
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4884981.svg)](https://doi.org/10.5281/zenodo.4884981)

Daniel Roush, Ana Giraldo-Silva, and Ferran Garcia-Pichel

<sup>1</sup>School of Life Sciences, Arizona State University, 85282 Tempe, Arizona, USA

<sup>2</sup>Center for Fundamental and Applied Microbiomics, Biodesign Institute, Arizona State University, 85282 Tempe, Arizona, USA

***
## **About Cydrasil**

Cydrasil is a comprehensive, curated, and community-built cyanobacterial reference package containing over 1300 16S rRNA gene
sequences with lengths exceeding 1100 base pairs. Cydrasil offers a curated alignment and a maximum-likelihood
phylogenetic tree that can be used for sequence placement or <i>de novo</i> phylogenetic reconstructions.
Cydrasil utilizes phylogenetic placement to give you a complete phylogenetic perspective of your new isolate or amplicon survey.

### **Current Stats:**
| Total Sequences: | 1327 |
|------------------|------|
| Cyanobacteria:   | 1288 |
| Sibling Clades:  | 34   |
| Plastids:        | 5    |

***
## **Package Contents**

| File/Folder Name                          | Description                                                                                                                                                            |
|-------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cydrasil-v3-reference-sequence-list.fasta | FASTA file containing the entire Cydrasil reference sequence set used as input for phylogenetic analysis                                                               |
| cydrasil-v3-database.json                 | JSON formatted database containing metadata about Cydrasil reference sequences. The file includes a link to the source repository and any warnings about the sequence. |
| cydrasil-v3-database.tsv                  | TSV formatted database containing metadata about Cydrasil reference sequences. The file includes a link to the source repository and any warnings about the sequence.  |
| cydrasil-v3-reference-alignment.afa       | Aligned FASTA formatted version of the Cydrasil reference alignment.                                                                                                   |
| cydrasil-v3-reference-alignment.phy       | Aligned relaxed PHYLIP formatted version of the Cydrasil reference alignment.                                                                                          |
| cydrasil-v3-ssu-align.bacteria.mask       | SSU-Align mask file for use with the SSU-Align version of the pipeline                                                                                                 |
| cydrasil-v3-reference-tree.nwk            | Newick formatted Cydrasil reference phylogenetic tree.                                                                                                                 |
| cydrasil-v3.bestModel                     | File containing model parameters for the generation of the reference tree. Needed for the model parameter specification (--model) for EPA-ng.                          |


***

## **Methodology**
Cydrasil was created originally as a comprehensive cyanobacterial 16S rRNA gene reference package to be used with phylogenetic placement algorithms like <a href="https://matsen.fhcrc.org/pplacer/" target="_blank">pplacer</a>, 
<a href="https://cme.h-its.org/exelixis/web/software/epa/index.html" target="_blank">RAxML epa</a>, and
<a href="https://github.com/Pbdas/epa-ng" target="_blank">EPA-ng</a>. When we originally populated the database,
we had strict inclusion criteria for reference sequences.
<br>
<ol>
    <li>The sequence must come from an isolated strain or a single-cell genome. Exceptions were made for metagenome-assembled
    genomes on a case by case basis after manual review of the genome (needed for most sibling clade sequences).</li>
    <li>Each reference sequence must be 1100 base pairs or longer. The minimum length was chosen as a compromise between
    strain coverage and sequence information for phylogenetic reconstruction. Of note, this excludes all
    cyanobacteria sequenced using the <a href="https://aem.asm.org/content/63/8/3327.long" target="_blank">Nübel et al. 1997</a>
    cyanobacteria-specific primers.</li>
</ol>

Cydrasil is populated with sequences collected from NCBI, JGI-IMG/M, and user submissions.
The reference alignment was generated using [SSU-Align](http://eddylab.org/software/ssu-align/)<sup>1</sup> with default parameters. This aligner uses a profile-based alignment strategy, in which each target sequence is aligned independently to a covariance model that uses the 16S rRNA gene secondary structure, and then masked using SSUMASK with the automatically computed alignment confidence values (posterior probabilities). A maximum-likelihood phylogenetic tree was then generated using the [RAxML-HPC2](https://cme.h-its.org/exelixis/web/software/raxml/)<sup>2</sup> Workflow on XSEDE (8.2.12) on the [CIPRES Science Gateway](http://www.phylo.org/)<sup>3</sup>. The ML + thorough bootstrap workflow was used with the following modified parameters: 1000 bootstraps (-N 1000) and the GTRGAMMA model. All other parameters were left at default values.  


***

## **How to Conduct a Local Sequence Placement Run**

1. ### **Alignment of query sequences to Cydrasil reference alignment**

    A FASTA file containing sequences of interest (typically Cyanobacterial sequences extracted from the reference sequences file output from Qiime 1/2) is aligned to the reference alignment. 

    Here you can use either **PaPaRa<sup>4</sup>** or **SSU-Align<sup>1</sup>** to align your query sequences to the Cydrasil reference alignment. The reference package contains a phylip (.phy) alignment (Cydrasil reference alignment) to use with PaPaRa.  

    >#### **Using  PaPaRa**  
    >[PaPaRa Information](https://cme.h-its.org/exelixis/web/software/papara/index.htm)  
    >[PaPaRa Githib](https://github.com/sim82/papara_nt)
    >
    >##### **PaPaRa Arguments**
    >| Flag | Description                                                                                | Cydrasil Filename                   |
    >|------|--------------------------------------------------------------------------------------------|-------------------------------------|
    >| -t   | Reference tree in newick (.nwk) format                                                     | cydrasil-v3-reference-tree.nwk      |
    >| -s   | Reference alignment in phylip (.phy) format                                                | cydrasil-v3-reference-alignment.phy |
    >| -q   | FASTA file containing sequences to be aligned (query sequences) to the reference alignment |                                     |
    >| -n   | Name of output alignment                                                                   |                                     |
    >| -r   | Prevent PaPaRa from adding gaps in the reference alignment                                 |                                     |
    >
    >##### **Example Command**
    >```
    >papara -t cydrasil-v3-reference-tree.nwk -s cydrasil-v3-reference-alignment.phy -q query-seqs.fasta -r -n combined-aln
    >```
    >

    >#### **Using SSU-Align**  
    >[SSU-Align Information](http://eddylab.org/software/ssu-align/)
    >
    >##### **SSU-Align Use**  
    >SSU-Align uses a workflow instead of just one command, but has the advantage of using the same alignment model as the Cydrasil reference alignment.  
    >**Importantly**, SSU-Align uses input order instead of input flags (-t) for parameters.  
    >The command ```ssu-align``` will align your query sequences to the SSU-Align 16S model.  
    >```
    >ssu-align query-seqs.fasta output-directory-name
    >```
    >##### **Example ```ssu-align``` Workflow**
    >```
    >ssu-align query-seqs.fasta aln
    >```
    >Mask the alignment using the mask file in the Cydrasil reference package
    >```
    >ssu-mask -s alignment.bacteria.mask aln/
    >```
    >Reformat the SSU-Align alignment from stockholm (.stk) to aligned fasta (.afa)
    >```
    >ssu-esl-reformat -o aligned-query-sequences-masked.afa afa aln/aln.bacteria.mask.stk
    >```
    >>Alternatively, the command ```ssu-prep -x``` allows for a multi-threaded alignment run on a desktop computer, but requires a few extra steps.  
    >>This is recommended for large query sequence files.  
    >>```
    >>ssu-prep -x query-seqs.fasta output-directory-name number-of-threads
    >>```
    >>
    >>#### **Example ```ssu-prep``` Workflow**
    >>```
    >>ssu-prep -x query-seqs.fasta aln 1
    >>```
    >>Output is a bash script: aln<!--This is a comment to prevent Markdown autolinking-->.ssu-align.sh  
    >>Running the script will execute the SSU-Align alignment
    >>```
    >>bash aln.ssu-align.sh
    >>```
    >>Cleanup the bash script
    >>```
    >>rm aln.ssu-align.sh
    >>```
    >>Mask the alignment using the mask file in the Cydrasil reference package
    >>```
    >>ssu-mask -s alignment.bacteria.mask aln/
    >>```
    >>Reformat the SSU-Align alignment from stockholm (.stk) to aligned fasta (.afa)
    >>```
    >>ssu-esl-reformat -o aligned-query-sequences-masked.afa afa aln/aln.bacteria.mask.stk
    >>```

2. ### **Conduct a sequence placement run using [EPA-ng](https://github.com/Pbdas/epa-ng)**
    Next, we use the aligned query sequences as the input into a sequence placement algorithm. We recommend [EPA-ng](https://github.com/Pbdas/epa-ng).

    #### **EPA-ng Arguments**
    | Flag    | Description                                     | Filename                                                             |
    |---------|-------------------------------------------------|----------------------------------------------------------------------|
    | -s      | Cydrasil reference alignment file in afa format | cydrasil-v3-reference-alignment.afa                                  |
    | -t      | Reference tree file                             | cydrasil-v3-reference-tree.nwk                                       |
    | -q      | Query sequence alignment                        | SSU-Align: aligned-query-sequences-masked.afa \| PaPaRa: query.fasta |
    | --model | Cydrasil model parameter specification file     | cydrasil-v3.bestModel                                                |
    | -w      | Output directory                                |                                                                      |
    | -T      | Number of threads for multithreading            |                                                                      |
    >**IMPORTANT NOTE**
    >If you used PaPaRa to align your query sequences, you need to run an extra command before you do placements to remove the reference sequences from the query alignment.
    >***This is a product of how PaPaRa was coded. If you skip this step, your output file will contain both query and reference sequences as placements.***
    >```
    >epa-ng --split cydrasil-v3-reference-alignment.phy papara_alignment.combined-aln
    >```
    >The output file from this command is ```query.fasta```  

    **Example EPA-ng Command**
    ```
    epa-ng -s cydrasil-v3-reference-alignment.afa -t cydrasil-v3-reference-tree.nwk -q aligned-query-sequences-masked.afa --model 
    ```
    **Output**

    EPA-ng outputs a .JPLACE file named ```placements.jplace```.

3. ### **Visualize and analyze your results**

    **Tree Visualization**

    To visualize the .JPLACE containing the sequences of interest, the placement file ```placements.jplace is uploaded onto [iTOL] (https://itol.embl.de/)<sup>5</sup>. Placements act as a dataset within iTOL and can be toggled. Nodes with sequences of interest are visualized with red circles and clicking a node will show a breakdown of sequence ids and the corresponding confidence values for that node. 

    Steps to visualize tree in iTOL:

    1. Create an user account with iTOL

    2. Upload (drag and drop) .jplace file into an iTOL project

    3. Reroot the tree by searching for **WOR1** and then clicking on its parent node (**I2504**) and navigating to **Tree structure > Re-root the tree here**

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
    >- Insert query sequence ID and and click on the sequence ID name to display red circles indicating phylogenic placement of a given query sequence.

***

## **References**
1. 	Nawrocki E. 2009. Structural RNA Homology Search and Alignment Using Covariance Models. Washington University School of Medicine.
2. 	Stamatakis A. 2014. RAxML version 8: A tool for phylogenetic analysis and post-analysis of large phylogenies. Bioinformatics 30:1312–1313.
3. 	Miller MA, Pfeiffer W, Schwartz T. 2010. Creating the CIPRES Science Gateway for inference of large phylogenetic trees. 2010 Gatew Comput Environ Work GCE 2010.
4. 	Berger SA, Stamatakis A. 2011. Aligning short reads to reference alignments and trees. Bioinformatics 27:2068–2075.
5. 	Letunic I, Bork P. 2016. Interactive tree of life (iTOL) v3: an online tool for the display and annotation of phylogenetic and other trees. Nucleic Acids Res 44:W242–W245.
