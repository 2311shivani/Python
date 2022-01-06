#2.Write a program which accept one number and display below pattern.

def PrintPattern(n):
          for i in range(n):
                    for j in range(n):
                              print(" * ", end = "  ")
                    print( " \n ")

n = int(input(" Enter the  number "))
PrintPattern(n)
