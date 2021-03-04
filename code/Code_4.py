import numpy as np
import matplotlib.pyplot as plt
X=[6,4,2,0,-2,-4,-6]
Prob=[1/7,1/7,1/7,1/7,1/7,1/7,1/7]
plt.stem(X,Prob,linefmt='green',label='theortical PMF')
#generating 1000 binomial samples for two x_1 and X_2
X_1=np.random.binomial(6,0.5,1000)
X_2=np.random.binomial(6,0.5,1000)
t=[]
for i in range(1000):
    t.append(X_1[i]-X_2[i])
prob=[]
c=0
for i in range(1000):
    if t[i]==6:
        c=c+1
prob.append(c/1000)
c=0
for i in range(1000):
    if t[i]==4:
        c=c+1
prob.append(c/1000)
c=0
for i in range(1000):
    if t[i]==2:
        c=c+1
prob.append(c/1000)
c=0
for i in range(1000):
    if t[i]==0:
        c=c+1
prob.append(c/1000)
c=0
for i in range(1000):
    if t[i]==-2:
        c=c+1
prob.append(c/1000)
c=0
for i in range(1000):
    if t[i]==-4:
        c=c+1
prob.append(c/1000)
c=0
for i in range(1000):
    if t[i]==-6:
        c=c+1
prob.append(c/1000)
plt.stem(X,prob,linefmt='red',markerfmt='D',label='Experimental PMF')
plt.xlabel('X')
plt.ylabel('PMF of X')
plt.title('PMF simulation')
plt.legend()
plt.show()

# pdf plot
cdf=[]
sum=0
for i in range(7):
    sum=sum+Prob[i]
    cdf.append(sum)
print(cdf)
plt.step(X,cdf,color='green',where='pre',label='theortical CDF')
cdf=[]
sum=0
for i in range(7):
    sum=sum+prob[i]
    cdf.append(sum)
plt.step(X,cdf,color='red',where='pre',label='experimental CDF')
plt.xlabel('X')
plt.ylabel('CDF')
plt.title('CDF Simulation')
plt.legend()
plt.show()

    
