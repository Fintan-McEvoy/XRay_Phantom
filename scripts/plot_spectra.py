def plot_spectra(KeV):
    setParams()
    spectral_data=spectra(KeV)
    plt.scatter(spectral_data[0],spectral_data[1])
    plt.figure(figsize=(1000,1000))
    plt.show()
