def display_images():
    fig = plt.figure()
    ax1 = fig.add_subplot(1,3,1)
    ax1.imshow(image_liver, cmap='gray_r',vmin=0,vmax=1)
    ax2 = fig.add_subplot(1,3,2)
    ax2.imshow(image_fat, cmap='gray_r',vmin=0,vmax=1)
    ax3 = fig.add_subplot(1,3,3)
    ax3.axes.set_xlabel("Air")
    ax3.imshow(image_air, cmap='gray_r',vmin=0,vmax=1)

    ax1.axes.get_xaxis().set_visible(False)
    ax1.axes.get_yaxis().set_visible(False)
    ax1.axes.set_title('Liver')

    ax2.axes.get_xaxis().set_visible(False)
    ax2.axes.get_yaxis().set_visible(False)
    ax2.axes.set_title('Fat')

    ax3.axes.get_xaxis().set_visible(False)
    ax3.axes.get_yaxis().set_visible(False)
    ax3.axes.set_title('Air')

    liver_mean = image_liver.mean()
    liver_std = image_liver.std()
    liver_snr = 10*np.log10(liver_mean/liver_std) # in db
    fat_mean = image_fat.mean()
    fat_std = image_fat.std()
    fat_snr = 10*np.log10(fat_mean/fat_std) # in db
    air_mean = image_air.mean()
    air_std = image_air.std()
    air_snr = 10*np.log10(air_mean/air_std) # in db


    print("Liver; Mean pixel value,",liver_mean)
    print("Liver; SNR, ", liver_snr, "db")
    print("Total number of photons reaching detector ", str(int(total_nr_photons*liver_mean)), end='\n\n')
    print("Fat; Mean pixel value,",fat_mean)
    print("Fat; SNR, ", fat_snr, "db")
    print("Total number of photons reaching detector ", str(int(total_nr_photons*fat_mean)), end='\n\n')
    print("Air; Mean pixel value,",air_mean)
    print("Air; SNR, ", air_snr, "db")
    print("Total number of photons reaching detector ", str(int(total_nr_photons*air_mean)), end='\n\n')
    
    contrast = np.log10(fat_mean/liver_mean)
    print ("Fat to liver contrast,", contrast)


