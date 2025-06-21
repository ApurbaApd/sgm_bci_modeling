import numpy as np
# from ..forward import ntf_local_stimulus as nt
from ..forward import ntf_local as nt
from scipy.stats import pearsonr
from ..utils import functions

def local_corr2(x,data,fvec):

    params = {
        "gei": x[0],
        "gii": x[1],
        "tau_e": x[2]/1000,
        "tau_i": x[3]/1000,
        # "pw": x[4]
        "pw": 0
        # "b": x[4],
        # "a": 0
    }
    # pw = x[4]
    htotal = nt.ntf_local(params,fvec)
    
    spectrum = np.abs(htotal)

    filtered = functions.mag2db(spectrum)
    
    pvalue = pearsonr(data, filtered)[1]
    
    return pvalue