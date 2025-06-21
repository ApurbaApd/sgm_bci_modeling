#!/bin/bash

#conda activate BCI_Handbook_Features_SubChapter #spectrome

# subid=( 0 1 2 3 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 )
subid=( 4 )

#subid=( 0 ) # ( 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18)

# nsub=( 0 1 2 3 4 5 6 7 8 9 10 11 12 13 )

for i in "${subid[@]}";
do python -u ../scripts/local_bci_rest_eeg.py ${i};
done

for i in "${subid[@]}";
do python -u ../scripts/local_bci_mi_eeg.py ${i};
done



