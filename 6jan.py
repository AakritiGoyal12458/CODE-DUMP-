import matplotlib.pyplot as plt
import numpy as np
x = np.array([5,7,8,7])
y = np.array([99,86,87,88])
#colors=np.array(["red","green","blue","purple"])
colors=np.array([90,80,0,30])
#colormap
#plt.scatter(x, y ,c=colors,cmap='viridis')
sizes=np.array([20,50,1000,300])
plt.scatter(x, y,s=sizes,alpha=0.5)
# x = np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
# y = np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])
# plt.scatter(x, y ,c="red" )
plt.colorbar()
plt.show()


import matplotlib.pyplot as plt
import numpy as np
x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x, y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()

#bar 
import matplotlib.pyplot as plt
import numpy as np
# x = np.array(["A", "B", "C", "D"])
# y = np.array([3, 8, 1, 10])
#width and height // horizntal and vertical
x = ["APPLES", "BANANAS"]
y = [400, 350]
plt.bar(x,y,color="red",width=0.1)
plt.show()
plt.barh(x,y,color="yellow",height=0.1)
plt.show()

import matplotlib.pyplot as plt
import numpy as np
age=[21,53,60,49,55,65,80]
plt.hist(age)
plt.xlabel("age grps")
plt.ylabel("population")
plt.title("histogram")
plt.show()
