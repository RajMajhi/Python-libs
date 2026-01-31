pip install matplotlib

import matplotlib
print(matplotlib.__version__)


import matplotlib.pyplot as plt

x = [2023 ,2024 , 2025 , 2026]
y = [39 , 60 , 50 , 30]

plt.plot(x,y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array ([2020, 2022, 2023, 2024, 2026])
y = np.array ([10, 30, 15, 30, 10])

plt.plot(x,y)
plt.show()

#Markers
import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 5])
y = np.array([0, 10])
plt.plot(x, y, 'o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023 ,2024 , 2025 , 2026])
y = np.array([39 , 60 , 50 , 30])


plt.plot(x,y,marker=".",
         ms=20,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         markeredgecolor="yellow",#mec
         linestyle="dashed"
        )
         

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023 ,2024 , 2025 , 2026])
y = np.array([39 , 60 , 50 , 30])


plt.plot(x,y,marker=".",
         ms=20,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         linestyle="dotted"
        )
         

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023 ,2024 , 2025 , 2026])
y = np.array([39 , 60 , 50 , 30])


plt.plot(x,y,marker=".",
         ms=20,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         markeredgecolor="yellow",#mec
         linestyle="dashdot"
        )
         

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023 ,2024 , 2025 , 2026])
y = np.array([39 , 60 , 50 , 30])


plt.plot(x,y,marker=".",
         ms=20,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         markeredgecolor="yellow",#mec
         linestyle="none"
        )
         

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023 ,2024 , 2025 , 2026])
y = np.array([0 , 30 , 20 , 40])


plt.plot(x,y,marker=".",
         ms=20,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         markeredgecolor="yellow",#mec
         linestyle="solid"
        )
         

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023 ,2024 , 2025 , 2026])
y = np.array([39 , 60 , 50 , 30])


plt.plot(x,y,marker=".",
         ms=20,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         markeredgecolor="yellow",#mec
         linestyle="solid",
         linewidth=5,
         color="pink"
        )
         

plt.show()

import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023 ,2024 , 2025 , 2026])
y = np.array([10 , 30 , 20 , 40])
y1 = np.array([10 ,25 , 15 , 29])

plt.plot(x,y,marker=".",
         ms=15,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         markeredgecolor="yellow",#mec
         linestyle="dashed",
         linewidth=2,
         color="darkblue"
        )

plt.plot(x,y1,marker=".",
         ms=15,#markersize
         mfc="red", #markerfacecolor # can use color picker for choosing colour.
         markeredgecolor="yellow",#mec
         linestyle="dashed",
         linewidth=2,
         color="blue"
        )
         

plt.show()

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



plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()

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


plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()

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



plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.show()

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



plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)

plt.xticks(x)
plt.show()


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


#Grid 
#grid() helps make plot easier to read by adding reference line.

import matplotlib.pyplot as plt
import numpy as np

x=[1, 2, 3, 4, 5, 6]
y=[2, 4, 6, 8, 10, 12]

plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=[1, 2, 3, 4, 5, 6]
y=[2, 4, 6, 8, 10, 12]

plt.grid() # initialization of grid
 
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=[1, 2, 3, 4, 5, 6]
y=[2, 4, 6, 8, 10, 12]

plt.grid(axis="y") # Customization of grid
 
plt.plot(x, y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

x=[1, 2, 3, 4, 5, 6]
y=[2, 4, 6, 8, 10, 12]

# Customization of grid
plt.grid(axis="y",
        linewidth=2,
        color="lightgrey",
        linestyle="dashed") 
 
plt.plot(x, y)
plt.show()


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

plt.bar(categories,values)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "fruits", "Vegetables", "Proteins", "Dairy", "Sweets"])
values= np.array([4, 3, 2, 5, 3, 6])

plt.bar(categories,values)
plt.title("Daily Consumption")
plt.xlabel("Food",size=10)
plt.ylabel("Quantity")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "fruits", "Vegetables", "Proteins", "Dairy", "Sweets"])
values= np.array([4, 3, 2, 5, 3, 6])

plt.bar(categories,values, color="green")
plt.title("Daily Consumption")
plt.xlabel("Food",size=10)
plt.ylabel("Quantity")

plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = np.array(["Grains", "fruits", "Vegetables", "Proteins", "Dairy", "Sweets"])
values= np.array([4, 3, 2, 5, 3, 6])

plt.barh(categories,values, color="lightgreen") # horizontal barchart
plt.title("Daily Consumption")
plt.xlabel("Food",size=10)
plt.ylabel("Quantity")

plt.show()

# pie chart
import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 245, 280, 270])

plt.pie(values, labels = categories)
plt.show()

# pie chart
import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 245, 280, 270])

plt.pie(values, labels = categories,
       autopct="%1f")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 245, 280, 270])

plt.pie(values, labels = categories,
       autopct="%1.1f")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 245, 280, 270])

plt.pie(values, labels = categories,
       autopct="%1.1f%%")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 245, 280, 270])
colors=["orange","blue","red","green"]

plt.pie(values, labels = categories,
       autopct="%1.1f%%",
       colors=colors)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 245, 280, 270])
colors=["orange","blue","red","green"]

plt.pie(values, labels = categories,
       autopct="%1.1f%%",
       colors=colors)

plt.title("College student strength")
plt.show()

import matplotlib.pyplot as plt
import numpy as np

categories = ["Freshman", "Sophomores", "Juniors", "Seniors"]
values = np.array([300, 245, 280, 270])
colors=["orange","blue","red","green"]

plt.pie(values, labels = categories,
       autopct="%1.1f%%",
       colors=colors,
       explode=[0,0,0,0.05])

plt.title("College student strength")
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
       shadow=True)

plt.title("College student strength")
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

#Scatter Graph - it shows the relationship betwween two variables helps to identify a correlation.
#(+,-,none), ex:- Study Hours vs Test Scores


import matplotlib.pyplot as plt
#import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7, 8] #hours studied
y = [50, 55, 60, 67, 75, 81, 90, 95, 99]# test scores

plt.scatter(x, y)
plt.show()


import matplotlib.pyplot as plt
#import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7, 8] # hours studied
y = [50, 55, 60, 67, 75, 81, 90, 95, 99]# Grades

plt.title("Test scores")
plt.xlabel("Hours studied")
plt.ylabel("Grade")

plt.scatter(x, y, color="blue")
plt.show()

import matplotlib.pyplot as plt
#import numpy as np

x = [0, 1, 2, 3, 4, 5, 6, 7, 8] # hours studied
y = [50, 55, 60, 67, 75, 81, 90, 95, 99]# Grades

plt.title("Test scores")
plt.xlabel("Hours studied")
plt.ylabel("Grade")

plt.scatter(x, y, color="blue",
           alpha = 0.55)
plt.show()

import matplotlib.pyplot as plt
#import numpy as np

x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8] # hours studied
y1 = [50, 55, 60, 67, 75, 81, 90, 95, 99]# Grades


x2 = [0, 1, 2, 3, 3, 5, 5, 6, 7] # hours studied
y2 = [50, 58, 63, 69, 77, 85, 92, 99, 101]# Grade

plt.title("Test scores")
plt.xlabel("Hours studied")
plt.ylabel("Grade")

plt.scatter(x1, y1, color="blue",
           alpha = 0.55,
           s = 200,
           )

plt.scatter(x2, y2, color="red",
           alpha = 0.55,
           s = 200
           )
plt.show()


import matplotlib.pyplot as plt
#import numpy as np

x1 = [0, 1, 2, 3, 4, 5, 6, 7, 8] # hours studied
y1 = [50, 55, 60, 67, 75, 81, 90, 95, 99]# Grades


x2 = [0, 1, 2, 3, 3, 5, 5, 6, 7] # hours studied
y2 = [50, 58, 63, 69, 77, 85, 92, 99, 101]# Grade

plt.title("Test scores")
plt.xlabel("Hours studied")
plt.ylabel("Grade")


plt.scatter(x1, y1, color="blue",
           alpha = 0.55,
           s = 100,
            label="ClassA"
           )

plt.scatter(x2, y2, color="red",
           alpha = 0.55,
           s = 100,
            label="ClassB"
           )
plt.legend()
plt.show() 
