# Code for PMF and CDF taking  n=100 
import numpy as np
import matplotlib.pyplot as plt
X=[]
for i in range(100):
    X.append(100-2*i)
X.append(-100)
Prob=[]
for i in range(101):
    Prob.append(1/101)
plt.stem(X,Prob,linefmt='green',label='theortical PMF')
X_1=np.random.binomial(100,0.5,1000)
X_2=np.random.binomial(100,0.5,1000)
t=[]
for i in range(1000):
    t.append(X_1[i]-X_2[i])
prob=[]
c=0
for i in range(100):
    k=100-2*i
    for j in range(1000):
        if t[j]==k:
            c=c+1
    prob.append(c/1000)
    c=0
for i in range(1000):
    if t[i]==-100:
        c=c+1
prob.append(c/1000)
plt.stem(X,prob,linefmt='red',markerfmt='D',label='Experimental PMF')
plt.xlabel('X')
plt.ylabel('PMF of X')
plt.title('PMF simulation')
plt.legend()
plt.show()

# Plot of CDF

cdf=[]
sum=0
for i in range(101):
    sum=sum+Prob[i]
    cdf.append(sum)
print(cdf)
plt.step(X,cdf,color='green',where='pre',label='theortical CDF')
cdf=[]
sum=0
for i in range(101):
    sum=sum+prob[i]
    cdf.append(sum)
plt.step(X,cdf,color='red',where='pre',label='experimental CDF')
plt.xlabel('X')
plt.ylabel('CDF')
plt.title('CDF Simulation')
plt.legend()
plt.show()

