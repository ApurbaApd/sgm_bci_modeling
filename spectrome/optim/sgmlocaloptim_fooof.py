import numpy as np
# from ..forward import ntf_local_stimulus as nt
from ..forward import ntf_local as nt
from scipy.stats import pearsonr
from ..utils import functions
from sklearn.metrics import mean_squared_error
from fooof import FOOOF

def local_corr(x,data,fvec):

    params = {
        "gei": x[0],
        "gii": x[1],
        "tau_e": x[2]/1000,
        "tau_i": x[3]/1000
    }

    htotal = nt.ntf_local(params,fvec)
    
    spectrum = np.abs(htotal)

    
    sgm_psd_scaled = ((spectrum-min(spectrum))/(max(spectrum)-min(spectrum)))*(max(data)-min(data)) + min(data)

    lower_limit = 2*(fvec[1]-fvec[0])
    fm = FOOOF(peak_width_limits=[lower_limit, 12.0])
    freq_range = [np.amin(fvec), np.amax(fvec)]

    data_features = np.zeros((5))
    sgm_features = np.zeros((5))

    fm.fit(fvec, data, freq_range)
    data_features[0] = 10*fm.get_params('aperiodic_params', 'exponent')
    if fm.n_peaks_ == 1:
        data_features[1] = fm.get_params('peak_params', 'CF')
        data_features[2] = fm.get_params('peak_params', 'CF')
        data_features[3] = 100*fm.get_params('peak_params', 'PW')
        data_features[4] = 100*fm.get_params('peak_params', 'PW')

    if fm.n_peaks_ > 2:
        ind = np.argsort(fm.get_params('peak_params', 'PW'))[::-1]
        data_features[1] = fm.get_params('peak_params', 'CF')[ind[0]]
        data_features[2] = fm.get_params('peak_params', 'CF')[ind[1]]
        data_features[3] = 100*fm.get_params('peak_params', 'PW')[ind[0]]
        data_features[4] = 100*fm.get_params('peak_params', 'PW')[ind[1]]

    if fm.n_peaks_ == 0:
        data_features[1] = np.amin(fvec)
        data_features[2] = np.amin(fvec)
        data_features[3] = 0
        data_features[4] = 0

    fm.fit(fvec, sgm_psd_scaled, freq_range)
    sgm_features[0] = 10*fm.get_params('aperiodic_params', 'exponent')
    if fm.n_peaks_ == 1:
        sgm_features[1] = fm.get_params('peak_params', 'CF')
        sgm_features[2] = fm.get_params('peak_params', 'CF')
        sgm_features[3] = 100*fm.get_params('peak_params', 'PW')
        sgm_features[4] = 100*fm.get_params('peak_params', 'PW')

    if fm.n_peaks_ > 2:
        ind = np.argsort(fm.get_params('peak_params', 'PW'))[::-1]
        sgm_features[1] = fm.get_params('peak_params', 'CF')[ind[0]]
        sgm_features[2] = fm.get_params('peak_params', 'CF')[ind[1]]
        sgm_features[3] = 100*fm.get_params('peak_params', 'PW')[ind[0]]
        sgm_features[4] = 100*fm.get_params('peak_params', 'PW')[ind[1]]

    if fm.n_peaks_ == 0:
        sgm_features[1] = np.amin(fvec)
        sgm_features[2] = np.amin(fvec)
        sgm_features[3] = 0
        sgm_features[4] = 0
    
    mse = mean_squared_error(data_features,sgm_features)

    return mse