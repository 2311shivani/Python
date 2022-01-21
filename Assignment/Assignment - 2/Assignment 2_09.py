#9.Write a program which accept number from user and return number of digits in that number.


def DigitNumber(No):

          Total = 0
          while(No > 0):

                No = No // 10
                Total = Total + 1

          return Total

def main():

    print(" Enter the Number ")
    No = int(input())

    result = DigitNumber(No)

    print(" Total Number of Digit is ", result)
                       
if __name__ == "__main__":
    main()
