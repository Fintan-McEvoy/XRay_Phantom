import os
cwd = os.getcwd()

exec(open(cwd+'/scripts/import_modules.py').read())
exec(open(cwd+'/scripts/readData.py').read())
exec(open(cwd+'/scripts/spectra.py').read())
exec(open(cwd+'/scripts/spectral_limits.py').read())
exec(open(cwd+'/scripts/monte_carlo_sample_batch.py').read())
exec(open(cwd+'/scripts/get_spectra_dependent_mu.py').read())
exec(open(cwd+'/scripts/create_images.py').read())
exec(open(cwd+'/scripts/display_images.py').read())
exec(open(cwd+'/scripts/phantom.py').read())
exec(open(cwd+'/scripts/hello.py').read())