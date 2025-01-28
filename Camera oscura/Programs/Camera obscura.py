import matplotlib.pyplot as plt
import numpy as np

dat=np.genfromtxt('../Data/obscerr.txt')
x=dat[:,0]
q=dat[:,1]
y=dat[:,2]
n=dat[:,3]

p=np.polyfit(x,y,1)
z=p[1]+p[0]*x

plt.errorbar(x,y, yerr=n ,ecolor='#0194d2', fmt='*', mfc='#0194d2', mec='#0194d2',label='Misure')
plt.plot(x,z,color='darkorange',label='Retta di best fit')
plt.grid(True)
plt.legend(numpoints=1, loc='upper left')
plt.xlabel('q/p')
plt.ylabel('i/o')
plt.title('Relazione tra ingrandimento e q/p')
plt.show()
print(p[0]) #A, sigA, B, sigB, delta
