#code 1 

import numpy as np
import matplotlib.pyplot as plt

x=np.array([80,85,90,95,100,105])
y=np.array([240,250,260,270,280,290])
#font
font1={'family':'serif','color':'blue','size':20}
font2={'family':'serif','color':'darkred','size':15}

plt.plot(x,y)
#title #location
plt.title("Marksheet",fontdict=font1,loc='left')
#label
plt.xlabel("student marks",fontdict=font2)
plt.ylabel("total",fontdict=font2)
plt.grid(color='red',ls='--',linewidth=2)
plt.show()


#code 2 
import matplotlib.pyplot as plt
import numpy as np

#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

plt.subplot(1, 2, 1)#1 row , 2 coloumns and plot is 1st priorit
plt.plot(x,y)
plt.title("SALES")

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

plt.subplot(1, 2, 2)
plt.plot(x,y)
plt.title("INCOME")

plt.show()

# question : make 6 plots 
    
#     1 2 3
#     4 5 6 
