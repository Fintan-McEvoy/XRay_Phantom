def phantom(mAs, KVp):
    setParams()
    if mAs <1:
        raise ValueError("mAs should be an integer between 1 and 10 inclusive")
    #if mAs >10:
    #    raise ValueError("mAs should be an integer between 1 and 10 inclusive")
    if KVp < 40:
        raise ValueError("KVp should be an integer between 40 and 120 inclusive")
    if KVp > 120:
        raise ValueError("KVp should be an integer between 40 and 120 inclusive")
    #mAs=100
    maxKeV=KVp
    #mAs=100
    #load_packages()
    read_data()
    spectra(KVp)
    spectral_limits()
    create_images(mAs,KVp)
    display_images()