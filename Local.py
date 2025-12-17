# # name = "mahi"
# # age =(24)
# # print(name,age)
# # a = 10
# # b = 20
# # print (a+b)
# # length = 200
# # breadth = 300
# # area =length+breadth
# # print(area)
# # name="credence"
# # version=3.22
# # is_esay=True
# # print(name)
# # print(version)
# # print(is_esay)
# # principal= 9500
# # rate= 0.99
# # time=1
# # simple_interest = (principal * rate * time) /6
# # print(simple_interest)

# # #unpacking 
# # a =[1,2,3,4,5,6,7,8,9,0]
# # p,*x,y,z= a
# # print("x:",x)
# # print("y:",y)
# # print("z:",z)
# # print("p:",p)

# # #Variables collectionName
# # collectionName = [1,2,3,4]
# # x, *y, z = collectionName
# # print(x)
# # print(y)
# # print(z)

# # a ="mahi"
# # def change():
# #     global a
# #     a= "umes"
# #     print(a)
# # change()
# # print(a)

# # num1 = 200
# # def addition():
# #     global num2
# #     num2 = 500
# # addition()
# # print("addition",num1+num2)

# name = "game"
# def newgamename():
#     global name
#     name = "GTA-6"
#     Price = [1000,2000,3000,4000,5000]
#     GTA,*FRYCAR,RDR2 = Price
#     print("GTA",GTA)
#     print("FRYCAR",FRYCAR)
#     print("RDR2",RDR2)
#     Price = 20000
#     onetime = 10000
#     principal= 9500
#     rate= 0.99
#     time=1
#     simple_interest = (Price * rate * time *principal) /3 /Price
#     print(simple_interest)
# # newgamename()



# ===================================Strings======================================================
# lineOfMind = """When You Expect
# - \"""more than others expectations\""",
# - it hurts more than others expectations"""
# print(len(lineOfMind))
# print (lineOfMind[1:4])

# # Array
# lchal = """i want to use py for\"Devops\" ---- after than use AWS i love DevOps"""
# print(lchal)
# print(len(lchal))
# print(lchal[5:5])


# ===================================Python Collections===================================
 
 
Name=["Saurabh","Chetan","Mahi","Bitu"]
print(len(Name))
print(Name[:])

# - Insert Item
stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
stdName.insert(0,1)
stdName.insert(3,"mahi")
print(stdName )
  
#   Append
stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
stdName.append("2025")
stdName.append("mahi")
print(stdName)


# Extend  
stdName = ["Chetan", "Yogesh", "Nilima", "Shivani", "Mayur","Pratiksha", "Lankesh", "Gayatri"]
stdRollNo = [1,2,3,4,5]
stdName.extend(stdRollNo)
print(stdName)
