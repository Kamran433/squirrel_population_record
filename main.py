# with open("weather-data.csv", "r") as doc:
#     # y = doc.read()
#     m = doc.readlines()
#     print(m)
import csv
import pandas
grey = 0
red = 0
black = 0
t = pandas.read_csv("weather-data.csv")
m = pandas.read_csv("squirrel.csv")
j = m["Primary Fur Color"]
lo = j.to_list()
for color in lo:
    if color == "Gray":
        grey += 1
    if color == "Cinnamon":
        red += 1
    if color == "Black":
        black += 1
print(grey)
print(red)
print(black)

print(lo)









# temperature = []
# only = []
# with open("weather-data.csv", "r") as doc:
#     data = csv.reader(doc)
#     # for dol in data:
#     #     temperature.append(dol)
#     # for i in range(1,len(temperature)):
#     #     temperature[i][1] = int(temperature[i][1])
#     # print(temperature)
#     for dol in data:
#        if dol[1] != "temp":
#           only.append(dol[1])
#     for i in range(len(only)):
#           only[i] = int(only[i])
#     print(only)

