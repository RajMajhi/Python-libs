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

#Grid 
#grid() helps make plot easier to read by adding reference line.
import matplotlib.pyplot as plt
import numpy as np

x=[1, 2, 3, 4, 5, 6]
y=[2, 4, 6, 8, 10, 12]

# Customization of grid
plt.grid(axis="y",
        linewidth=2,
        color="lightgrey",
        linestyle="dotted") 
 
plt.plot(x, y)
plt.show()

#BarChart
#barchart compare categories of data by representing each category with a bar.

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "fruits", "Vegetables", "Proteins", "Dairy", "Sweets"])
values= np.array([4, 3, 2, 5, 3, 6])

plt.bar(categories,values, color="green")

plt.barh(categories,values, color="lightgreen") # horizontal barchart

plt.title("Daily Consumption")
plt.xlabel("Food",size=10)
plt.ylabel("Quantity")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 245, 280, 270])
colors=["orange","blue","red","green"]

plt.pie(values, labels = categories,
       autopct="%1.1f%%",
       colors=colors,
       explode=[0,0,0,0.1],
       shadow=True,
       startangle=180)

plt.title("College student strength")
plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
figure, axes = plt.subplots(2,2)

axes[0, 0].plot(x, x*2,color="blue")
axes[0, 0].set_title("x*2")
axes[0, 1].bar(x, x**2, color="red")
axes[0, 1].set_title("x**2")
axes[1, 0].plot(x, x**3, color="green")
axes[1, 0].set_title("x**3")
axes[1, 1].plot(x, x**4, color="purple")
axes[1, 1].set_title("x**4")

plt.tight_layout()
plt.show()
