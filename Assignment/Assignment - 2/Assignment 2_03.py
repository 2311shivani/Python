#3. Write a program which accept one number from user and return its factorial.

def PrintFactorial(No):
          Fact = 1
          while (No > 0):
                    Fact = Fact * No
                    No = No - 1
          return Fact

def main():

    print(" Enter the number for Factorial ")
    No = int(input())

    result = PrintFactorial(No)

    print(" Factorial of Number is ", result)

if __name__ == "__main__":
    main()










