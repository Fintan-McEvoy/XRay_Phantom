def create_images(mAs,maxKeV):
    mAs_factor = KV_quant_factor.loc[KV_quant_factor['KV']== maxKeV]['mAs']
    mAs = mAs * mAs_factor.item()
    print(mAs_factor.item())
    global total_nr_photons
    total_nr_photons = 10*100*mAs# factor 10 is in the montecarlo script so evene mAs 1 has 10 photons, 100 is 10X10 pixles
    
    global image_fat
    image_fat = np.zeros((10,10))
    for  i in range (0,10,1):
        print("working on pixel row " + str(i+1)  +" out of 10 for image 1 of 3     ", end='\r')
        for j in range (0,10,1):
            spectrum_samples = pd.DataFrame(monte_carlo_sample_batch(mAs, maxKeV), columns=['keV'])
            spect_dependent_mu=pd.merge(spectrum_samples,mu_fat,on='keV',how='left')
            image_fat[i,j]= np.power(10,(-1*spect_dependent_mu['mu'].mean()))
        #time.sleep(1)
    print("",end='\n')
    #image_fat

    global image_liver
    image_liver = np.zeros((10,10))
    for  i in range (0,10,1):
        for j in range (0,10,1):
            spectrum_samples = pd.DataFrame(monte_carlo_sample_batch(mAs, maxKeV), columns=['keV'])
            spect_dependent_mu=pd.merge(spectrum_samples,mu_liver,on='keV',how='left')
            image_liver[i,j]= np.power(10,(-1*spect_dependent_mu['mu'].mean()))
            print("working on pixel row " + str(i+1)  +" out of 10 for image 2 of 3     ", end='\r')
        #time.sleep(1)
    print("",end='\n')
    #image_liver

    global image_air
    image_air = np.zeros((10,10))
    for  i in range (0,10,1):
        for j in range (0,10,1):
            spectrum_samples = pd.DataFrame(monte_carlo_sample_batch(mAs, maxKeV), columns=['keV'])
            spect_dependent_mu=pd.merge(spectrum_samples,mu_air,on='keV',how='left')
            image_air[i,j]= np.power(10,(-1*spect_dependent_mu['mu'].mean()))
            print("working on pixel row " + str(i+1)  +" out of 10 for image 3 of 3     ", end='\r')
    print("",end='\n')
    print("",end='\n')
    #time.sleep(1)
    #clear_output()    
