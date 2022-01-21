#10. Write a program which accept number from user and return addition of digits in that number.

def Number(No):

            Digit = 0
            Add = 0
                
            while(No > 0):

                Digit = No % 10
                Add = Add + Digit
                No = No // 10
                             
            return Add

def main():

    print(" Enter a Number ")
    No = int(input())

    result = Number(No)

    print(" Addition of Digit Number ", result)

if __name__ == "__main__":
    main()

