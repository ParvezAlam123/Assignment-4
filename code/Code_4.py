# Here I am generating binomial 1000 samples and calculating the value of X
# X= difference between number of heads and number of tails
import numpy as np
s=np.random.binomial(6,0.5,1000)
for i in range(1000):
    s[i]=s[i]-(6-s[i])
print("Values of X for 10000 sample is :")
print(s)

