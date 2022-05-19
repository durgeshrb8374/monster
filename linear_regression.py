import  matplotlib.pyplot as plt
import numpy as np
#input values
x = np.array([10,9,2,15,10,16,11,16])
y = np.array([95,80,10,50,45,98,38,93])


plt.plot(x,y,"ro")

slope , intercept = np.polyfit(x,y,1)
y = slope*x + intercept

plt.plot(x,y,"bo")


plt.plot(x,y,'-b',label = "y=mx+c")
plt.ylabel("Risk Score on a scale of o-100")
plt.xlabel("No. of hours spent  on Driving")

plt.show()