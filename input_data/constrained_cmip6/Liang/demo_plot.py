import numpy as np
import seaborn as sns; sns.set()
import matplotlib.pyplot as plt
import pandas as pd
from   netCDF4 import Dataset as open_ncfile

## read csv file
data_his =pd.read_csv('../cdf_his.csv')

## import variable 
whis=data_his['cdf']
ehis=data_his['cdf_e']
ehism=data_his['mean_e']
whism=data_his['mean_w']

year=np.arange(1996, 2015)

w_his_05=[]
w_his_95=[]
e_his_05=[]
e_his_95=[]
whis_m=[]
ehis_m=[]

for i in range(np.size(year)):
    ## for every year, read weighted results with 5% and 95% percentitle and means 
    his_05=float(whis[i].strip('][').split(',')[5])
    his_95=float(whis[i].strip('][').split(',')[95])
    his_mw=whism[i]
    w_his_05=np.append(w_his_05,his_05)
    w_his_95=np.append(w_his_95,his_95)
    whis_m=np.append(whis_m,his_mw)

    ## for every year, read unweighted results with 5% and 95% percentitle and means
    ehis_05=float(ehis[i].strip('][').split(',')[5])
    ehis_95=float(ehis[i].strip('][').split(',')[95])
    ehis_me=ehism[i]
    e_his_05=np.append(e_his_05,ehis_05)
    e_his_95=np.append(e_his_95,ehis_95)
    ehis_m=np.append(ehis_m,ehis_me)
