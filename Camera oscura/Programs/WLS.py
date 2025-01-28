import numpy as np
import matplotlib.pyplot as plt

dat=np.genfromtxt('../Data/obscerr.txt')
x=dat[:,0]
xe=dat[:,1]
y=dat[:,2]
ye=dat[:,3]

w=(1/ye**2)

sumw = np.sum(w)
sumwx2 = np.sum(w*x**2)
sumwx = np.sum(w*x)
sumwy = np.sum(w*y)
sumwxy = np.sum(w*x*y)

delta = sumw*sumwx2-(sumwx)**2
A = (sumwx2*sumwy-sumwx*sumwxy)/(delta)
B = (sumw*sumwxy-sumwx*sumwy)/(delta)

z = A+B*x

plt.errorbar(x,y,yerr=ye,xerr=xe, fmt='.r')
plt.plot(x,z, color='blue')
plt.show()
print(B)
