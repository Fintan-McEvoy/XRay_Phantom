def get_spectra_dependent_mu(spectrum_samples):
    global spect_dependent_mu
    spect_dependent_mu=pd.merge(spectrum_samples,mu_fat,on='keV',how='left')
