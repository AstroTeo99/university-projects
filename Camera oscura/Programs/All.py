import numpy as np
import matplotlib.pyplot as plt

dat=np.genfromtxt('../Data/obscerr.txt')
x=dat[:,0]
xe=dat[:,1]
y=dat[:,2]
ye=dat[:,3]

pesi=1/(ye**2)

p=np.polyfit(x,y,1) #non pesato
z=p[1]+p[0]*x

#f=np.polyfit(x,y,1,w=pesi) #pesato con polyfit
#g=f[1]+f[0]*x

sumw = np.sum(pesi)
sumwx2 = np.sum(pesi*x**2)
sumwx = np.sum(pesi*x)
sumwy = np.sum(pesi*y)
sumwxy = np.sum(pesi*x*y)

delta = sumw*sumwx2-(sumwx)**2
A = (sumwx2*sumwy-sumwx*sumwxy)/(delta)
B = (sumw*sumwxy-sumwx*sumwy)/(delta)
sigA = (sumwx2/delta)**(1/2)
sigB = (sumw/delta)**(1/2)

l = A+B*x #pesato con minimi quadrati

#Correlazione = varianza / errore x * errore y
xm = np.mean(x)
ym = np.mean(y)
sumxxmyym = np.sum((x-xm)*(y-ym))
sumxxm2 = np.sum((x-xm)**2)
sumyym2 = np.sum((y-ym)**2)
r = sumxxmyym/np.sqrt(sumxxm2*sumyym2) #Correlazione

plt.errorbar(x,y,xerr=xe, yerr=ye ,ecolor='#0194d2', fmt='.', mfc='#0194d2', mec='#0194d2',label='Misure')
plt.plot(x,z, color='red', label='Retta di best fit (non pesata)')
#plt.plot(x,g, color='green', label='W Polyfit')
plt.plot(x,l,color='darkorange',label='Retta di best fit (pesata)')
plt.legend(numpoints=1, loc='upper left')
plt.xlabel('q/p')
plt.ylabel("-y'/y")
plt.title("Relazione di dipendenza tra -y'/y e q/p")
plt.grid(True)
plt.ylim([-0.015,0.7])
plt.xlim([-0.015,0.7])
plt.show()
print(A,sigA,B,sigB,r, p[1], p[0])
