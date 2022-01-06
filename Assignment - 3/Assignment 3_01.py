#1.Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

def addition():
    list = ()
    add = 0
No = int(input(" Number of Element:"))

for i in range(0,No):
    int(input(" Enter the Number "))

for element in range(0,len(list)):
     add = add + list[i]
   
print("Addion of Elements in given list is:", addition())


