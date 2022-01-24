import scipy.io as sio
import scipy
import numpy as np
import matplotlib.pyplot as plt
import math


Number=input("Please tell me the number of the Sample you want to display: ")

#Load File
test = sio.loadmat(sio.loadmat(os.path.realpath("Data_For_Test.py")))

#Get the gesture; 
x=test["Data_rand"][int(Number)][0][0][0]


#Equation
x=20*np.log10(abs(x)/np.amax(abs(x)))


#Display Spectogram
plt.imshow(x,vmin=-50, vmax=0,cmap='jet', aspect='auto')
plt.colorbar()
plt.show()
