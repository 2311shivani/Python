#4.Write a program which accept N numbers from user and store it into List. Accept one another number from user and return frequency of that number from List.

def number(List):

    cnt = 0

    print(" Enter the Number of Element ")
    Src_Ele = int(input())

    for i in range(len(List)):

        if(List[i] == Src_Ele):
            cnt = cnt + 1

    return cnt

def main():
    List = []
    Ele = 0 

    print(" Enter the element ")
    No = int(input())

    for i in range(0,No):
        Ele = int(input(" Enter the Element "))
        List.append(Ele)

    print(" Given the list ", List)

    ret = number(List)

    print(" Enter the number of Search element ", ret)

if __name__ == "__main__":
    main()
