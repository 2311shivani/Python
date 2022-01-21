#2.Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

def Number(List):
    Max = 0

    for i in range(len(List)):
        if(List[i] > Max):
            Max = List[i]

    return Max

def main():
    List = []
    Ele = 0

    print(" Enter the number of element ")
    No = int(input())

    for i in range(0,No):
         Ele = int(input(" Enter the Element: "))
         List.append(Ele)

    print(" Given list is ", List)

    ret = Number(List)

    print(" Maximum element is ", ret)

if __name__ == "__main__":
    main()
