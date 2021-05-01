import pandas
import os
#import csv

folder = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(
    folder, "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# with open(data_file) as data:
#     weather = csv.reader(data)
#     temp = []
#     for row in weather:
#         if row[1] != "temp":
#             temp.append(int(row[1]))

#     print(temp)

#weather = pandas.read_csv(data_file)
# print(weather["temp"])  # dictonary?

#temp_list = weather["temp"].to_list()
#average = sum(temp_list) / len(temp_list)
# print(weather["temp"].max())

#print(weather[weather.temp == weather.temp.max()])
# monday = weather[weather.day == "Monday"]
# far = (monday.temp * 1.8) + 32
# print(far)

# data_dict = {
#     "student": ["Lauren", "Amy", "Jacob", "Matt"],
#     "score": [69, 57, 62, 89]
# }

# data = pandas.DataFrame(data_dict)
# data.to_csv("Python/PythonCourse/Day25/student_scores.csv")

squirrel_info = pandas.read_csv(data_file)
# gray = 0
# red = 0
# black = 0
# for colour in squirrel_info["Primary Fur Color"]:
#     if colour == "Gray":
#         gray += 1
#     elif colour == "Cinnamon":
#         red += 1
#     elif colour == "Black":
#         black += 1


gray = len(squirrel_info[squirrel_info["Primary Fur Color"] == "Gray"])
red = len(squirrel_info[squirrel_info["Primary Fur Color"] == "Cinnamon"])
black = len(squirrel_info[squirrel_info["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Colour": ["Gray", "Red", "Black"],
    "count": [gray, red, black]
}

new_data = pandas.DataFrame(data_dict)
new_data.to_csv("Python/PythonCourse/Day25/fur_colours.csv")
