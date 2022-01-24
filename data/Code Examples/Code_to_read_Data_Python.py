
#This code will display a Doppler Micro-Doppler Spectogram that will help
#you familiarize with the data
# By choosing the Person, Gesture and the Repeat, you will see that certain
# data displayed in a Spectogram


import scipy.io as sio
import scipy
import numpy as np
import matplotlib.pyplot as plt
import math
import os

 #Here you must specify the sample you want to see
person=input("Please tell me the person letter(A, B, C, D, E or F): ")
gesture=input('Please tell me the gesture( Wave =0, Pinch=1, Swipe=2, Click =3): ')
sample=input('Please tell me repeat number: ')


#Load File; Get the path from the file containing the Data
test = sio.loadmat(os.path.realpath("Data_Per_PersonData_Training_Person_"+person+".mat")) 

#Get the gesture; 
x=test["Data_Training"]["Doppler_Signals"][0][0][0][int(gesture)][int(sample)][0]


#Equation
x=20*np.log10(abs(x)/np.amax(abs(x)))

#Display Spectogram
plt.imshow(x,vmin=-50, vmax=0,cmap='jet', aspect='auto',extent=[0,x.shape[1],-501,500]) 



plt.ylabel("Doppler",fontsize=17)
plt.xlabel("Time",fontsize=17)

plt.colorbar()
plt.show()
