#!/bin/bash
# Bash shell script created by ssu-prep for running 6 ssu-align jobs.
# Each job will process a separate partition of the sequence file:
# 'cydrasil-v3-sequence-list.fasta'.
#
# This script will execute all 6 jobs at once, in parallel. It is only
# meant to be executed on a system with 6 cpus/cores. The first 5 jobs
# will run in the background and output to /dev/null. The final job will
# output to STDOUT, allowing you to follow its progress.
#
# The final job is special, after computing its alignments it will wait for all
# other jobs to finish and then merge the output of all jobs together.
# The merged output files will be in the directory: '/cydrasil-3-ssu-align/'
#
# The for loop below will execute/submit the first 5 of 6 jobs.
# The final ssu-align job is executed separately because it does the merging.
#
for (( i=1; i<=5; i++ ))
do
	echo "# Executing: ssu-align cydrasil-3-ssu-align/cydrasil-v3-sequence-list.fasta.$i cydrasil-3-ssu-align/cydrasil-3-ssu-align.$i > /dev/null &"
	ssu-align cydrasil-3-ssu-align/cydrasil-v3-sequence-list.fasta.$i cydrasil-3-ssu-align/cydrasil-3-ssu-align.$i > /dev/null &
done
echo "# Executing: ssu-align --merge 6 cydrasil-3-ssu-align/cydrasil-v3-sequence-list.fasta.6 cydrasil-3-ssu-align/cydrasil-3-ssu-align.6"
ssu-align --merge 6 cydrasil-3-ssu-align/cydrasil-v3-sequence-list.fasta.6 cydrasil-3-ssu-align/cydrasil-3-ssu-align.6
