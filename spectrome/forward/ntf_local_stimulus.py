import numpy as np

def ntf_local(parameters,freqs):
    tau_e = parameters["tau_e"]
    tau_i = parameters["tau_i"]
    # speed = parameters["speed"]
    gei = parameters[
        "gei"
    ]  # excitatory-inhibitory synaptic conductance as ratio of E-E syn
    gii = parameters[
        "gii"
    ]  # inhibitory-inhibitory synaptic conductance as ratio of E-E syn
    a = parameters["a"]
    b = parameters["b"]
#     gee = parameters["gee"]
    # print(a)
    
    gee = 1
    
    Htotal_stim_l = []
    
    for freq in freqs:
        w = 2 * np.pi * freq

        Fe = np.divide(1 / tau_e ** 2, (1j * w + 1 / tau_e) ** 2)
        Fi = np.divide(1 / tau_i ** 2, (1j * w + 1 / tau_i) ** 2)

        Hed = (1 + (Fe * Fi * gei)/(tau_e * (1j * w + Fi*gii/tau_i)))/(1j * w + Fe*gee/tau_e + (Fe * Fi * gei)**2/(tau_e * tau_i * (1j * w + Fi * gii / tau_i)))

        Hid = (1 - (Fe * Fi * gei)/(tau_i * (1j * w + Fe*gee/tau_e)))/(1j * w + Fi * gii/tau_i + (Fe * Fi * gei)**2/(tau_e * tau_i * (1j * w + Fe*gee / tau_e)))

        Htotal = Hed + Hid
        
        Htotal_stim = np.abs(Htotal)**2 * (1 + b**2/(a**2 + w**2))
        
        Htotal_stim_l.append(Htotal_stim)
        
    Htotal_stim_l = np.asarray(Htotal_stim_l)
    
    return np.sqrt(Htotal_stim_l)