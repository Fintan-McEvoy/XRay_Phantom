def spectra(x):
    keV=x
    global spectral_data
    spectral_data = pd.read_csv('spectra/'+str(keV)+"_spectrum.csv", header=None)
    spectral_data = spectral_data.T
    return spectral_data
