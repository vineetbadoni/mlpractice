#Q-Q plot
import numpy as np
import pylab
import scipy.stats as stats

#N(0,1)
# loc is mean(mu), scale is std deviation(sigma)
std_normal = np.random.normal(loc=0,scale=1,size=1000)

for i in range(0,101):
    print(i,np.percentile(std_normal,i))

#Generate the 100 Normal observed values
measurements = np.random.normal(loc=20,scale=5,size=1000000)
#try with size 1000

#Compare obsereved values with the standard values
#probplot plots 2 distributions for comaprison around a line.
stats.probplot(measurements,dist="norm",plot=pylab)

pylab.show()