# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:11:31 2020

@author: guokai
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from matplotlib.pyplot import MultipleLocator
font = {'family' : 'Arial',
'weight' : 'normal',
'size'   : 25}
df_EMI=pd.read_csv(r'EMI.csv')
RL=[]
THK=[]
x=np.linspace(0,5,201)
y=np.linspace(2000000000,18000000000,201)
# y=np.linspace(26500000000,40000000000,201)
e1=df_EMI['e1']
e2=df_EMI['e2']
u1=df_EMI['u1']
u2=df_EMI['u2']
df_EMI['sqrt_erur']=np.sqrt((e1-e2*1j)*(u1-u2*1j))
df_EMI['sqrt_ur_er']=np.sqrt((u1-u2*1j)/(e1-e2*1j))

def f(X,Y):
    Y=Y*1E9
    pifd_c=X*Y*np.array(df_EMI['2pi_c']).reshape(-1,1)
    #print(pifd_c)
    tanh_x=np.tanh(pifd_c*np.array(df_EMI['sqrt_erur']).reshape(-1,1)*1j)
    Z_in=np.array(df_EMI['sqrt_ur_er']).reshape(-1,1)*tanh_x
    #print(Z_in)
    return 20*np.log10(np.abs((Z_in-1)/(Z_in+1)))

    
plt.figure(figsize=(16,10))
ax=plt.axes(projection='3d')

y=y/1E9
X,Y=np.meshgrid(x,y)
z=f(X,Y)
ax=plt.gca()
y_major_locator=MultipleLocator(5)
x_major_locator=MultipleLocator(1)
ax.yaxis.set_major_locator(y_major_locator)
ax.xaxis.set_major_locator(x_major_locator)
ax.set_xlabel('Thickness (mm)',labelpad=20)
ax.set_ylabel('Frequency (GHz)',labelpad=20)
ax.set_zlabel('Reflection loss (dB)',labelpad=20)
plt.tick_params(labelsize=20) 
surf=ax.plot_surface(X,Y,z,rstride=1,cstride=1,cmap = plt.get_cmap('rainbow'))
plt.colorbar(surf).ax.tick_params(labelsize=20)
#ax.contour(X, Y, z, zdir = 'z', offset = -50, cmap = plt.get_cmap('rainbow'))
#ax.contour(X, Y, z, zdir = 'y', offset = 8, cmap = plt.get_cmap('rainbow'))
#ax.contour(X, Y, z, zdir = 'x', offset = 5, cmap = plt.get_cmap('rainbow'))
ax.set_xlabel('Thickness (mm)',font)
ax.set_ylabel('Frequency (GHz)',font)
ax.set_zlabel('Reflection loss (dB)',font)
plt.xlim(5,0);plt.ylim(18,1)
#ax.set_zlim(-50,5)
# plt.savefig('MgO.jpg',dpi=600,bbox_inches='tight')
# ax.view_init(elev=0, azim=90)
# plt.savefig('MgO_T.jpg',dpi=600,bbox_inches='tight')
# ax.view_init(elev=90, azim=0)
# plt.savefig('MgO_TF.jpg',dpi=600,bbox_inches='tight')
# ax.view_init(elev=0, azim=180)
# plt.savefig('MgO_F.jpg',dpi=600,bbox_inches='tight')