#3.Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

def number(List):
    Min = 0

    for i in range(len(List)):

        if(i == 0):
            Min = List[i]
            continue

        if(List[i] < Min):
            Min = List[i]

        return Min

def main():
    List = []
    Ele = 0
    
    print("Enter the number of element ")
    No = int(input())

    for i in range(0,No):
        Ele = int(input(" Enter the number "))
        List.append(Ele)

    print(" Given the Number of list ", List)

    ret = number(List)

    print(" Minimum number Given is ", ret)


if __name__ == "__main__":
        main()
