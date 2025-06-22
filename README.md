## Set up
First clone the environment to your computer, either download this repo as a `.zip` file or `git clone https://github.com/ApurbaApd/sgm_bci_modeling.git`.

Set up a [conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) if you do not have all the packages/compatible versions. The list of dependencies is listed in `environment.yml`.

Set-up environment using conda, detailed instructions can be found [here](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). Or after cloning this repository, go to the repo by typing `cd spectrome` and then typing:
`conda env create -f environment.yml`

If conda complains about not finding packages/libraries, make sure `conda-forge` is in the list of channels being searched by `conda`.
You may add `conda-forge` to your list of channels with the command: `conda config --add channels conda-forge`.

The default name of the environment is `spectrome`, activate the environment with `source activate spectrome`, and deactivate with `source deactivate` or `conda deactivate`.

If you want to be able to run `spectrome` from anywhere, just add it's path to your PYTHONPATH. For instance, if you downloaded `spectrome` to `~/Documents/spectrome` do `export PYTHONPATH=$PYTHONPATH:~/Documents/spectrome`. You may have to restart your terminal to make sure this change takes effect.

After completing the set-up for conda environment and `spectrome` path, you may go to the `spectrome` folder and type `jupyter notebook` or `jupyter lab` in your terminal to run the Jupyter notebooks.

## Files:
 - `../spectrome/notebooks`: contains 15 jupyter notebooks, with all the analysis done on the data.
 - `../spectrome/scripts`: It contains `run_local_model_mi_apd.py`, and `run_local_model_mi_apd.py` scripts to run the local model in the case of MI and Rest, respectively, which is the simulation of frequency spectrums with various values of the parameters in different bounds. 

 - `../spectrome/data_brain_plotting`: contains jupyter notebook for brain plots.
    - 'plot_brain_mne.ipynb`: For plotting brain regions.
