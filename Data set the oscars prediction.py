print("Best Picture Winners 2023-2013")

import pandas as pd 
df = pd.read_excel("OSCAR WINNERS BP.xlsx") 
print(df)


print("Sex Differences in a starring role")
import matplotlib.pyplot as plt
import numpy as np
plt.title("Sex of starring role")
y = np.array([40,60])
mylabels = ["Female","Male"]

plt.pie(y, labels = mylabels)
plt.show()
#
print("Sex of co-starring role")
import matplotlib.pyplot as plt
import numpy as np
plt.title("Sex of co-starring role")
y = np.array([10,90])
mylabels = ["Female","Male"]
myexplode = [0, 0.2]
plt.pie(y, labels = mylabels,colors=['rosybrown', 
'grey'],explode = myexplode,shadow = True,
autopct='%1.1f%%')
plt.show() 
#
print("Genre")

import matplotlib.pyplot as plt
import numpy as np
plt.title("Genre ")
x = np.array(["Comedy", "Drama", "Thriller", "Romance", "Crime", "Musical"])
y = np.array([4, 4, 4, 2, 1, 1])



plt.bar(x,y color = "red")
plt.show()


# Ethnicity of lead actor winner
print("Ethnicity of lead actor")
import matplotlib.pyplot as plt
import numpy as np
plt.title("Ethnicity of the lead actor")
x = np.array(["American", "English/British", "South Korean", "Chinese"])
y = np.array([5, 3, 1, 1])

plt.bar(x,y, color = "green")
plt.show()

# Ethnicity of support actor winner

print("Ethnicity of supporting actor")
import matplotlib.pyplot as plt
import numpy as np
plt.title("Ethnicity of the supporting actor")
x = np.array(["American", "German-Irish", "South Korean", "Han Chinese"])
y = np.array([7, 1, 1, 1])

plt.bar(x,y)
plt.show()

print("Oscar Nominations")
import matplotlib.pyplot as plt
import numpy as np
plt.title("Oscar Nominations")
x = np.array(["2023","2022","2021","2020","2019","2018","2017","2016","2015","2014"])
y = np.array([11, 3, 6, 6, 5, 13, 8, 6, 9, 9])

plt.bar(x,y)
plt.show()

#age rating winner
import statistics 
print(statistics.mode([15,12,12,15,12,15
                       ,15,15,15,15]))


print("Sex Differences in a starring role")
import matplotlib.pyplot as plt
import numpy as np
plt.title("Sex of starring actor")
y = np.array([40,60])
mylabels = ["Female","Male"]
myexplode = [0, 0.2]
plt.pie(y, labels = mylabels,colors=['rosybrown', 
'grey'],explode = myexplode, shadow = True,
autopct='%1.1f%%')
plt.show()

#age rating mean code nom
import statistics 
print(statistics.mode([
    12,15,15,15,15,15,12,12,15,
    12,12,12,15,12,12,12,15,15,12,
    15,15,12,15,15,12,12,15,15,12,
    18,15,12,0,15,15,12,12,12,15,12,
    15,15,15,15,15,12,15,15,15,12,1,15,15
    ,15,12,12,12,1,1,15,15,15,12,12,15,15,
    15,12,15,15,15,15,12,12,12,15,15,12,15,
    12,15,15,12,15,18,12,15,12,18,12,1,12,15,15
]))



#other oscar awards won
import statistics 
print(statistics.mode([1,0,0,0,4,0,1,1,2,1,1,0,1,
                       0,5,0,0,2,0,1,2,2,2,1,2,3,2
                       ,1,2,3,2,1,1,0,3,1,4,1,3,3,
                       1,1,0,1,3,2,4,1,0,2,3,0,2,
                       1,1,6,0,0,2,3,1,1,0,1,2,6,
                       0,1,4,1,4,1,1,1,3,0,0,3,7,
                       1,0,0,3,0,1,3,0,2,3,4,
                       2,1,1]))





#total number of oscar nom
import statistics 
print(statistics.mode([6,9,11,7,6,9,8,4,4,3,12,7,3,
                       6,7,10,4,4,10,6,5,6,6,6,6,6,
                       6,11,6,10,10,4,6,6,10,7,6,5
                       ,10,5,10,8,8,5,4,8,7,13,6,2,6
                       ,8,4,6,4,7,14,3,6,6,12,5,6,7
                       ,4,6,10,3,6,9,6,9,8,2,5,5,10
                       ,6,6,10,5,6,4,9,5,5,7,4,5,8,
                       11,12,8,5]))


#total baftas won
import statistics 
print(statistics.mode([0,4,1,0,1,7,4,1,1,2,2,2,1,1,
                       1,5,0,0,1,0,2,3,2,1,1,2,2,3
                       ,1,1,7,1,1,1,0,1,1,2,7,1,4
                       ,1,1,1,1,1,5,3,1,0,2,0,0,1
                       ,1,1,5,0,2,1,5,1,1,0,1,1,4
                       ,1,0,1,3,5,0,0,3,3,3,1,0,6
                       ,0,0,1,2,0,2,3,0,2,4,2,1,1
                       ,0]))





#Rotten tomato score mode
import statistics 
print(statistics.mode([94,94,93,99,77,93,98
                       ,97,91,95]))

x = range(91,99)
for n in x:
  print(n)

#Rotten tomato score range
x = range(77,99)
for n in x:
  print(n)

#Rotten tomato score range WITHOUT 77
x = range(91,99)
for n in x:
  print(n)

#METACRITIC
import statistics 
print(statistics.mode([81,72,88,96,69,87,99,93,87
                       ,96]))

x = range(72,99)
for n in x:
  print(n)



import matplotlib.pyplot as plt
import numpy as np
plt.title("Release date - month")
y = np.array([40, 30, 20, 10])
mylabels = ["Jan", "Feb", "May", "Aug"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]
myexplode = [0.1,0,0,0]
plt.pie(y, labels = mylabels,explode = myexplode
        , shadow = True,colors = mycolors)
plt.show() 

#baftr awards won mode
import statistics 
print(statistics.mode([
1,2,3,2,1,3,0,1,1,2]))

#range baftas awards
x = range(0,3)
for n in x:
  print(n)


# total baftas nom
import statistics 
print(statistics.mode([
10,3,7,4,4,12,4,3,10,10]))

#range b awards nom
x = range(3,12)
for n in x:
  print(n)

# distrubution
import matplotlib.pyplot as plt
import numpy as np
plt.title("Distribution Company")
x = np.array([ "Searchlight Pictures","A24",
               "Universal Pictures", 
               " Camera Film","Apple TV","Entertainment One"])
y = np.array([4, 2, 1, 2, 1, 1])
ypoints = np.array([0,1,2,3,4])

plt.barh(x, y, height = 0.3,color="violet")
plt.show()

color="violet"


#total award nom

#awards nom
x = range(123,350)
for n in x:
  print(n)


#awards won
x = range(23,401)
for n in x:
  print(n)

#awards oscars nom
import statistics 
print(statistics.mode([11,3,6,6,5,13,8,6,9,9]))


x = range(6,13)
for n in x:
  print(n)

#awards won
x = range(58, 401)
for n in x:
  print(n)
  
#oscar nom
import statistics 
print(statistics.mode([11,6,6,5,13,8,6,9,9]))

#runtime
x = range(111,139)
for n in x:
  print(n)



















































