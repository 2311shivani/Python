#4.Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

list = []
no = int(input(" Enter the Number of Element: "))
for i in range(1,no + 1):
            x = int(input(" Enter the element: "))
            list.append(x)
Number = 0
num = int(input(" Enter the number of Search: "))
for j in list:
    if(j == num):
        Number = Number + 1
print(" number of times ", num, " appears is ", Number)
