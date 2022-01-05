#9.Write a program which display first 10 even numbers on screen.

def evennumber(n):
          i = j = 1
          while j <= n:
                    if i % 2 == 0:
                              print(i,end = "  ")
                              j = j + 1
                    i = i + 1

n = int(input(" Enter the  number "))
evennumber(n)
