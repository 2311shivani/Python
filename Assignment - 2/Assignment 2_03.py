#3. Write a program which accept one number from user and return its factorial.

def PrintFactorial(n):
          i = 1
          while n > 0:
                    i = i * n
                    n = n - 1
          return i

X = int(input(" Enter the number "))
print("Factorial ",X,PrintFactorial(X))











