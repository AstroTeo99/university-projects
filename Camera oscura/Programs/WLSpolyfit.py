import numpy as np
import matplotlib.pyplot as plt

dat=np.genfromtxt('../Data/obscprova.txt')
x=dat[:,0]
xe=dat[:,1]
y=dat[:,2]
ye=dat[:,3]

pesi=1/(ye**2)

p=np.polyfit(x,y,1,w=pesi)
z=p[1]+p[0]*x

plt.errorbar(x,y,yerr=ye,xerr=xe, fmt='.r')
plt.plot(x,z, color='blue')
plt.show()
print(p[0])
