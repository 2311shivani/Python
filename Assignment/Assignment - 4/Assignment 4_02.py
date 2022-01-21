#2.Write a program which contains one lambda function which accepts two parameters and return its multiplication.

Multiplication = lambda a,b : a*b

def main():

    print(" Enter the two number of Multiplication ")

    No1 = int(input(" Enter First number "))
    No2 = int(input(" Enter Second number "))

    ret = Multiplication(No1,No2)

    print(" Multiplication of Two Number is ", ret)

if __name__ == "__main__":
    main()
    
