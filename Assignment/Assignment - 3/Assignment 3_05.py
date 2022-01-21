#5.Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List. Main python file accepts N numbers from user and pass eachnumber to ChkPrime() function which is part of our user defined module named as Marvellous Num. Name of the function from main python file should be ListPrime().

import MarvellousNum as M

def Prime(List):
    Prime_List = []
    No = 0

    for i in List:
        No = M.chk_Prime(i)
        if(No == " Number is Prime "):
            Prime_List.append(i)

    return Prime_List

def Add_Prime_List(List):
    Add = 0
    for i in range(Len(List)):
        Add = Add + List[i]

    return Add

def main():

    List = []
    Ele = 0

    print(" Enter the Element ")
    No = int(input())

    for i in range(0,No):
        Ele = int(input(" Enter the Element "))
        List.append(Ele)

    print(" Given list is ", List)

    ret = Prime(List)

    print(" Prime list is  ", ret)

    Addition = Add_Prime_List(ret)

    print(" Addition of Prime List is ", Addition)

if __name__ == "__main__":
    main()
