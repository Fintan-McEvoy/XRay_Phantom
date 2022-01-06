def read_data():
    import pandas as pd
    global mu_liver
    mu_liver=pd.read_csv("./mu_values_tissues/mu_liver_complete.csv", header=0)
    global mu_fat
    mu_fat = pd.read_csv("./mu_values_tissues/mu_fat_complete.csv", header=0)
    global mu_air
    mu_air = pd.read_csv("./mu_values_tissues/mu_air_complete.csv", header=0)
    global KV_quant_factor
    KV_quant_factor = pd.read_csv("./KV_mAs_5_PercentRule/data_KV_mAs.csv", header = 0)

read_data()


