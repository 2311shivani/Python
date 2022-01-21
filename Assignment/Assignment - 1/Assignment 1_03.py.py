#3.Write a program which contains one function named as Add() which accepts two numbers from user and return addition of that two numbers.

def add(No1,No2):

    Ret = 0

    Ret = No1 + No2

    return Ret
def main():

    print(" Enter First Number ")
    no1 = int(input())

    print(" Enter Second Number ")
    no2 = int(input())

    Add = no1 + no2

    print("Addition is two Number", Add)

if __name__ == "__main__":
    main()
