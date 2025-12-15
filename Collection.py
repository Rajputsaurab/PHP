collectionname = [1,2,3,]
x,y,z = collectionname
print(x)
print(y)
print(z)
a = "sam"
def greet():
    print("Ssup",a)
greet()    


num1=5
def addition():
    global num2
    num2 = 10
addition()
print("addition of num1 and num2", num1 + num2)    

def greet():
 a= "Local" #local variable
 print("Hello", a)
greet()