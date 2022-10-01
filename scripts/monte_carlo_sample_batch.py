def monte_carlo_sample_batch(mAs, maxKeV):
    factor=(spectral_data.shape[0]-1)/maxKeV
    num_samples = int(10*mAs)
    samples = np.zeros(num_samples)
    
    batch_size = 128
    num_total_accepted_samples = 0
    while num_total_accepted_samples < num_samples:
        randX = np.random.uniform(low=minKeV,high=maxKeV,size=batch_size)
        randY = np.random.uniform(low=0.0,high=maxInt,size=batch_size)
        randIndex = np.random.uniform(low=0, high=spectral_data.shape[0]-1, size=batch_size)
        
        # Filter the candidate samples based on the target spectrum
        #accepted_samples_mask = np.logical_and(randY < spectral_data[1][np.round(factor*randX)], randY > 0)
        accepted_samples_mask = np.logical_and(randY < spectral_data[1][np.round(randIndex)], randY > 0)
        accepted_samples = np.round(randX[accepted_samples_mask])
        
        samples_left = num_samples - num_total_accepted_samples
        update_from = num_total_accepted_samples
        update_to = num_total_accepted_samples + np.min([samples_left, len(accepted_samples), batch_size])
        samples[update_from:update_to] = accepted_samples[0:np.min([samples_left, len(accepted_samples), batch_size])]
        
        num_total_accepted_samples = num_total_accepted_samples + len(accepted_samples)
    
    return(samples)
