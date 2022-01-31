#1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all the functions from Arithmetic module by accepting the parameters from user.

import Arithmetic as A

def main():

    print(" Enter The First Number ")
    No1 = int(input())

    print(" Enter the Second Number ")
    No2 = int(input())

    ret = A.Addition(No1, No2)
    print(" Addition of Number is ",ret)

    ret = A.Substraction(No1, No2)
    print(" Substraction of Number is ",ret)

    ret = A.Multiplication(No1, No2)
    print(" Multiplication of Number is ",ret)

    ret = A.Division(No1, No2)
    print(" Division of Number is ",)

if __name__ == "__main__":
    main()
