#7.Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false.

def Number(Num):

    if(Num %5 == 0):
        print(" Number is divisible by 5")
    else:
        print(" Number is not divisible by 5")

def main():
    print(" Enter the number ")
    Num = int(input())

    result = Number(Num)

if __name__ == "__main__":
    main()



        
