# # # # # Create a list with 5 different data types.
# # # # list=["1","2","ravi","sam","mahi"]
# # # # print(list[:])

# # # # # 2. Find the length of a list without counting manually.
# # # # numbers = [10, 20, 30, 40, 50]
# # # # length = len(numbers)
# # # # print(length)

# # # # # 3. Access the first and last elements of a list using indexing.
# # # # Name = ["mahesh","amruta","ravi","saurabh","Kunal"]
# # # # numbers = [1,2,]
# # # # Name.extend(numbers)
# # # # print(Name)

# # # # # 4. Access the last element using negative indexing.
# # # # Name = ["mahesh","amruta","ravi","saurabh","Kunal"]
# # # # numbers = [1,2,3,4,5,6,7]
# # # # Name.extend(numbers)
# # # # print("First element:", Name[0])
# # # # print("Last element:", Name[-1])

# # # # # 5. Check whether "Python" exists in a list.
# # # # languages = ["Java", "C", "C++", "Python", "JavaScript"]
# # # # languages.remove("Java")
# # # # print(languages[2])

# # # # # # 6. Convert a tuple into a list.
# # # # # tuple1 = (1,2,3,4,5,6,7,8,9)
# # # # # tuple2 = ("a","b","c","d","e")
# # # # # list1 = list(tuple1)
# # # # # list2 = list(tuple2)
# # # # # print(type(list1), type(list2))

# # # # # 7. Convert a list into a tuple.
# # # # stdclass = [1,2,3,4,5,6,7,8,9,0]
# # # # stdroll = tuple(stdclass)
# # # # print(stdclass)
# # # # print(type(stdroll))

# # # # # 8. Create a tuple with only one element.
# # # # stdtubal = (100,)
# # # # print(type(stdtubal))
# # # # print(stdtubal)

# # # # # 9. Create a set with duplicate values and print it.
# # # # set = {1,2,3,4,5,6,7,8,1,2,3,4,5,6,9,0}
# # # # print(set)
# # # # for value in set :
# # # #     print(value)

# # # # # 11. Change the second element of a list.
# # # # my_set = [10,20,30]
# # # # my_set[1]= 99
# # # # print(my_set)

# # # # # 12. Replace the first three elements of a list using slicing.
# # # # ReplaceReplace = [100,200,300,400]
# # # # ReplaceReplace[:3]=[10,20,30]
# # # # print(ReplaceReplace)

# # # # # 13. Insert "AWS" at index position 1 in a list.
# # # # tech = ["Linux", "Docker", "Kubernetes"]
# # # # tech.insert(1, "AWS")
# # # # print(tech)


# # # # tech = ["Linux", "Docker", "Kubernetes"]
# # # # tech.append("Linux")
# # # # print(tech)


# # # # tech = ["Linux", "Docker", "Kubernetes"]
# # # # tech.extend("Linux")
# # # # print(tech)

# # # # tech = ["Linux", "Docker", "Kubernetes"]
# # # # tech.remove("Linux")
# # # # print(tech)

# # # # tech = ["Linux", "Docker", "Kubernetes"]
# # # # tech.pop()
# # # # print(tech)

# # # # tech = ["Linux", "Docker", "Kubernetes"]
# # # # tech.sort()
# # # # print(tech)

# # # # tech = ["Linux", "Docker", "Kubernetes"]
# # # # tech.sort(reverse=True)
# # # # print(tech)

# # # # my_set.reverse()
# # # # print(my_set)

# # # # a = ["apple","banana"]
# # # # b = a
# # # # b.append("cat")
# # # # print(b)

# # # # a = ["apple","banana"]
# # # # b = a.copy()
# # # # b.append("cat")
# # # # print(b)


# # # # a = ["apple","banana"]
# # # # b = ["home","cat"]
# # # # c = a + b 
# # # # print(c)

# # # # a = ("apple","banana")
# # # # b = ("home","cat")
# # # # aList = list(a)
# # # # bList = list(b)
# # # # aList.extend(bList)
# # # # print(aList)
# # # # # print(type(c))
 
# # # # 25. Join two tuples using the += operator.

# # # # t1 = (1, 2)
# # # # t2 = (3, 4)
# # # # t1 += t2
# # # # print(t1)

# # # # s = {1, 2}
# # # # l = [3, 4, 5]
# # # # s.update(l)
# # # # print(s)


# # # # t = (1, 2, 3, 4, 5)
# # # # a, b, *c = t
# # # # print(a, b, c)

# # # # s1 = {1, 2, 3}
# # # # s2 = {2, 3, 4}
# # # # print(s1 & s2)
# # # # print(s1 - s2)
# # # # print(s1 ^ s2)

# # # # my_list = [10, 3.14, "Python", True, [1, 2]]
# # # # print(my_list)
# # # # print(len(my_list))

# # # # 1. Create a dictionary with keys name, age, and city and print the dictionary.
# # # d = {"name": "Amit", "age": 22, "city": "Pune"}
# # # print(d)
# # # # 2. Access and print the value of key "name" from a dictionary.
# # # print(d["name"])
# # # # 3. Find the length of a dictionary using len().
# # # print(len(d))
# # # # 4. Check the data type of a dictionary using type().
# # # print(type(d))
# # # # 5. Create a dictionary using the dict() constructor from a tuple of key-value pairs.
# # # g = ("name","age", "city")
# # # f = ("rohit", "37", "mumbai")
# # # newdict= dict.fromkeys(g,f)
# # # print(newdict)

# # # t = (("name", "Rohit"), ("age",37), ("city", "Mumbai"))
# # # d2 = dict(t)
# # # print(d2)
# # # # 6. Use the get() method to access a key that exists in the dictionary.
# # # print(d2.get("name"))

# # # # 7. Add a new key "rollNo" with value 25 to an existing dictionary.
# # # d2["rollNo"] = 45
# # # print(d2)
# # # # 8. Remove the key "address" from a dictionary using pop().
# # # d2.pop("rollNo")
# # # print(d2)
# # # # 9. Clear all elements from a dictionary using the clear() method.
# # # d2.clear()
# # # print(d2)


# # # # 10. Write an if statement to check whether a number is positive or negative.
# # # num = 18
# # # if num > 0:
# # #      print("The number is positive")
# # # if num < 0:
# # #      print("The number is negative")

# # # # 11. Duplicate Keys in a Dictionary
# # # student = {"name": "Umesh", "name": "Mahi"}
# # # print(student)

# # # # 12. Check if "college" exists using in
# # data = {"name": "Rohit", "age": 37}
# # if "college" in data:
# #     print("Key exists")
# # else:
# #     print("Key does not exist")

# # # 13. Update the value of "city" in a dictionary using the update() method.
# # user = {"name": "Virat", "city": "India"}
# # user.update({"city": "London"})
# # print(user)

# # # 14. Copy one dictionary into another using the copy() method and prove both are independent.
# # newteam = user.copy()
# # newteam["city"] = "Bangalore"   
# # print(newteam)

# # # 15. Remove the last inserted item from a dictionary using popitem().

# # car = {"brand": "Tesla", "model": "Model 3", "year": 2025}
# # removed_item = car.popitem()
# # print(f"Removed: {removed_item}")
# # print(f"Current Dictionary: {car}")

# # # 16. Write a program to print all keys and values using keys() and values().
# # info = {"Name": "Sam", "Field": "Data Science"}
# # print("Keys:", list(info.keys()))
# # print("Values:", list(info.values()))

# # # 17. Write an if–else program to check whether a number is even or odd.
# # n = 45
# # if n % 2 == 0:
# #     print("Even")
# # else:
# #     print("Odd")

# # Even = 18
# # if Even % 2 == 0:
# #     print("Even")
# # else:
# #     print("Odd")

    
# # # 18. Write a program using elif to check whether a number is positive, negative, or zero.
# # x = 0
# # if x > 0:
# #     print("Positive")
# # elif x < 0:
# #     print("Negative")
# # else:
# #     print("Zero")

# # # 19. Write a nested if statement to check if a person is eligible to vote
# # # (gender = "female" and age ≥ 18)gender = "female"
# # age = 20
# # gender="female"
# # if gender == "female":
# #     if age >= 18:
# #         print("Eligible to vote")
# #     else:
# #         print("ypu are not eliguible")

# # # 20. Use a shortcut if–else to print "Pass" or "Fail" based on marks.
# # marks = 100
# # print("Pass" if marks >= 35 else "Fail")

# # # 21. Create a dictionary and use a loop to print all key-value pairs using items().
# # student = {
# #     "name": "Saurabh",
# #     "age": 22,
# #     "course": "DevOps"
# # }
# # for key, value in student.items():
# #     print(key, ":", value)

# # # 22. Write a program to check if a key exists in a dictionary and print an appropriate message
# # student = {
# #     "name": "Saurabh",
# #     "age": 22,
# #     "course": "DevOps"
# # }

# # key_to_check = "age"

# # if key_to_check in student:
# #     print("Key exists in the dictionary")
# # else:
# #     print("Key does not exist in the dictionary")


# # # 23. Create two dictionaries. Copy one into another using assignment (=) and show how changes affect both.
# # # Create first dictionary
# # dict1 = {
# #     "name": "Saurabh",
# #     "age": 22,
# #     "city": "Nashik"
# # }


# # dict2 = dict1

# # print("Before change:")
# # print("dict1 =", dict1)
# # print("dict2 =", dict2)

# # dict2["age"] = 24

# # print("\nAfter change:")
# # print("dict1 =", dict1)
# # print("dict2 =", dict2)

# # # 24. Write a program that takes a dictionary and prints only keys whose values are integers.

# # data = {
# #     "name": "Mahi",
# #     "age": 24,
# #     "city": "Pune",
# #     "marks": 85,
# #     "is_student": True,
# #     "rollno":34
# # }

# # print("Keys with integer values:")
# # for key, value in data.items():
# #     if type(value) == int:
# #         print(key)

# # # 25. Use setdefault() to insert a key "grade" if it does not exist.
# # student = {
# #     "name": "Umesh",
# #     "age": 26,
# #     "marks": 90,
# #     "pass": 2020,
# #     "working": "brighter future",
# #     "role": "DevOps engineer"   

# # }

# # student.setdefault("grade", "A+")

# # print(student)

# # # 26. Write a program using logical operators (and, or, not) inside an if condition.

# student = 100
# school =  30
# totalTeachers = 12
# if student < school and student > school:
#     print("Both conditions are true")
# if student < school or school > totalTeachers or student > school:
#     print("at least one condition is true")
# if not student > school:
#     print("student is not less than school")

# # 27. Write a program using pass inside an if statement.
# student = 100
# school =  30
# if student < school :
#     pass
# else:
#     print("inside")


# # 28. Write a match statement to display a message based on the day name (Monday, Tuesday, etc.).
def monday = input("Enter day in display:-").lower()
match monday:
    case "monday":
        print("Start of the work week.")
    case "tuesday":
        print("Second day of the week.")
    case "wednesday":
        print("Midweek day.")
    case "thursday":
        print("Almost there!")
    case "friday":
        print("End of the work week.")
    case "saturday":
        print("Weekend! Time to relax.")
    case "sunday":
        print("Enjoy your Sunday.")
    case _:
        print("Invalid day name.")


# 29. Use a match statement with multiple values in one case to categorize students.
grade = input("Enter student grade: ").upper()

match grade:
    case "A" | "A+":
        print("Excellent student")
    case "B" | "B+":
        print("Good student")
    case "C" | "C+":
        print("Average student")
    case "D":
        print("Needs improvement")
    case "F":
        print("Fail")
    case _:
        print("Invalid grade")

# 30. Write a match statement with an extra condition using if to check name and age.
name =input("Enter Name:-")
age =24
match name:
    case "sam" | "rohit" |  "virat" if age == 24:
        print("Candidate into 1st Class")
    case  "shubham" | "doni" | "ABD" if age == 26:
        print("Candidate into 2st Class") 
    case _:
        print("There is no any Candidate with this name")    
   
    