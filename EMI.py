# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 17:08:24 2020

@author: guokai
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.pyplot import MultipleLocator
import xlwt
font = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 25}
df_EMI=pd.read_csv(r'EMI.csv')
RL=[]
THK=[]
RL_min=[]
e1=df_EMI['e1']
e2=df_EMI['e2']
u1=df_EMI['u1']
u2=df_EMI['u2']
df_EMI['sqrt_erur']=np.sqrt((e1-e2*1j)*(u1-u2*1j))
df_EMI['sqrt_ur_er']=np.sqrt((u1-u2*1j)/(e1-e2*1j))

plt.figure(figsize=(14,10))
for i in np.linspace(0,5,201):
    thk=i
    df_EMI['2pifd_c']=df_EMI['2pi_c']*df_EMI['f']*thk

    df_EMI['tanh_x']=np.tanh(df_EMI['2pifd_c']*df_EMI['sqrt_erur']*1j)
    df_EMI['Z_in']=df_EMI['sqrt_ur_er']*df_EMI['tanh_x']
    df_EMI['RL']=20*np.log10(np.abs((df_EMI['Z_in']-1)/(df_EMI['Z_in']+1)))
    RL.append(df_EMI['RL'].tolist())
    #THK.append(thk)
    RL_min.append(min(df_EMI['RL']))
    # df_EMI['f'][np.argmin(df_EMI['RL'])]
    plt.plot(df_EMI['f']/1E9,df_EMI['RL'],label=str(i))
    #plt.legend(['5','4.22','4.215','4.210','4.205','4.20','4.195','4.19','4.185','4.18','4'])
    #plt.legend()
    plt.xlabel('Frequency (GHz)',font)
    plt.ylabel('Reflection loss (dB)',font)
    plt.tick_params(labelsize=20)
print('RL最小值为', min(RL_min))
thk_list=np.linspace(0,5,201).tolist()
print('RL最小值对应的厚度为', thk_list[np.argmin(RL_min)])
#ax=plt.axes(projection='3d')
#x=THK
#y=df_EMI['f']/1E9
#z=RL
#ax=plt.gca()
#y_major_locator=MultipleLocator(1)
#x_major_locator=MultipleLocator(1)
#ax.yaxis.set_major_locator(y_major_locator)
#ax.xaxis.set_major_locator(x_major_locator)
#plt.tick_params(labelsize=20) 
#ax.contour3D(x,y,z,500,cmap='viridis',rstride=1,cstride=1,edgecolor='none')
#ax.set_xlabel('Thickness (mm)',font)
#ax.set_ylabel('Frequency (GHz)',font)
#ax.set_zlabel('Reflection loss (dB)',font)
#ax.view_init(elev=0, azim=0)
