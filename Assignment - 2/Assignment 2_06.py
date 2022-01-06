#6. Write a program which accept one number and display below pattern.


def printpattern(n):
          for i in range(n):
                    j = i + 1
                    while j <= n:
                              print(" * ", end = " ")
                              j += 1
                    print(" \n ")

X = int(input(" Enter the number "))
printpattern(X) 
