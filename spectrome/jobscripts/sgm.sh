#!/bin/bash
#$ -S /bin/bash
#$ -cwd
#### Specify job name
#$ -N rs1_sess4_eeg_corr_f
#### Output file
#$ -o ~/research/bci_results/jobout/$JOB_NAME_$JOB_ID.out
#### Error file
#$ -e ~/research/bci_results/jobout/$JOB_NAME_$JOB_ID.err
#### Number of tasks
#$ -t 1-19:1
#### number of cores 
#$ -pe smp 2
#### Specify queue
#$ -q long.q
#### memory per core
#$ -l mem_free=2G
#### Maximum run time 
#$ -l h_rt=336:00:00

# export PATH="/home/pverma2/software/miniconda3/bin:$PATH"
export PATH="/wynton/protected/home/rad-wynton-only/pverma2/software/miniconda3/bin:$PATH"
source activate spectrome
set -exu


export MKL_NUM_THREADS=1
export NUMEXPR_NUM_THREADS=1
export OMP_NUM_THREADS=1


nproc --all

which python 

python -u ../scripts/local_bci_rest_eeg.py $((${SGE_TASK_ID}-1))
# python -u ../scripts/local_bci_rest.py 

# [[ -n "$JOB_ID" ]] && /netopt/sge_n1ge6/bin/lx24-amd64/qstat -j "$JOB_ID"
[[ -n "$JOB_ID" ]] && qstat -j "$JOB_ID"