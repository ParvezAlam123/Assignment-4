# Here I am generating binomial 1000 samples and calculating the value of X
# X= difference between number of heads and number of tails
import numpy as np
import matplotlib.pyplot as plt
s=np.random.binomial(6,0.5,1000)
for i in range(1000):
    s[i]=s[i]-(6-s[i])
    plt.scatter(i,s[i],color='green')
print("Values of X for 10000 sample is :")
print(s)
plt.xlabel('number of bernoulli sample')
plt.ylabel('value of X')
plt.title("scatter plot for X")
plt.show()


