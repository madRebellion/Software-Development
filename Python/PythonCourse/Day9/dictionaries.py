#Dictionaries

#student_scores = {
#  "Harry": 81,
#  "Ron": 78,
#  "Hermione": 99, 
#  "Draco": 74,
#  "Neville": 62,
#}
#
#student_grades = {}
#
#for score in student_scores:
#    grade = student_scores[score]
#    if grade > 90:
#        student_grades[score] = "Outstanding"
#    elif grade > 80:
#        student_grades[score] = "Exceeds Expectations"
#    elif grade > 70:
#        student_grades[score] = "Acceptable"
#    else:
#        student_grades[score] = "Fail"
#
#print(student_grades)

#Nesting dictionaries in lists

#travel_log = [
#{
#  "country": "France",
#  "visits": 12,
#  "cities": ["Paris", "Lille", "Dijon"]
#},
#{
#  "country": "Germany",
#  "visits": 5,
#  "cities": ["Berlin", "Hamburg", "Stuttgart"]
#},
#]
#
#def add_new_country(country, times_visited, cities):
#    new_dict = {}
#    new_dict["country"] = country
#    new_dict["visits"] = times_visited
#    new_dict["cities"] = cities
#    travel_log.append(new_dict)
#
#add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#print(travel_log)

#Silent Auction

from hammer_art import logo
print(logo)

dict = {}
people_to_add = True

while people_to_add:
    user_name = input("What is your name? ")
    bid = float(input("How much do you want to bid? £"))
    dict[user_name] = bid
    result = input("Do you want to include more people? Yes or No\n").lower()
    if result == "no":
        people_to_add = False

highest_value = 0
person = ""
for key in dict:    
    if dict[key] > highest_value:
        highest_value = dict[key]
        person = key

print(f"{person} bidded the highest with £{dict[person]}")