#1.Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List.

def addition(List):
    
    add = 0
    for i in range(len(List)):
        add = add + List[i]

    return add

def main():
    List = []
    Ele = 0

    print(" Enter the Number ")
    No = int(input())

    for i in range(0, No):
        Ele = int(input(" Enter the Element "))
        List.append(Ele)

    print(" Given List is ", List)

    ret = addition(List)

    print(" Addion of Elements in given list is:", ret)

if __name__ == "__main__":
    main()
