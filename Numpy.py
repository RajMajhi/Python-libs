#NUMPY lib

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023 ,2024 , 2025 , 2026])
y = np.array([10 , 30 , 20 , 40])
y1 = np.array([10 ,25 , 15 , 29])
y2 = np.array([10 ,35 , 25 , 39])
rx = dict(marker=".",
         ms=10,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         markeredgecolor="yellow",#mec
         linestyle="dotted",
         linewidth=1,
        )
plt.plot(x, y, color="red", **rx)
plt.plot(x, y1,color="green", **rx)
plt.plot(x, y2,color="blue", **rx)

plt.show()


#Label
import matplotlib.pyplot as plt
import numpy as np

x= np.array ([2023, 2024, 2025, 2026])
y1= np.array ([15, 25, 30, 20])
y2= np.array ([17, 23, 38, 5])
y3= np.array ([13, 15, 20, 30])

plt.title("Class size", fontsize=20, 
          family="Arial", 
          fontweight="bold",
          color="green"
         )

plt.xlabel("Year",fontsize=20, 
          family="Arial", 
          fontweight="bold",
          color="blue")

plt.ylabel("Students",fontsize=20, 
          family="Arial", 
          fontweight="bold",
          color="blue")

plt.tick_params(axis="both",
               colors="red")


plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)
plt.show()


plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()
