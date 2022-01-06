def spectral_limits():
    global maxInt
    maxInt=np.ceil(max(spectral_data[1]))
    maxInt
    global maxKeV
    maxKeV=max(spectral_data[0])
    maxKeV
    global minKeV
    minKeV=min(spectral_data[0][spectral_data[1].gt(0.01*maxInt)])
