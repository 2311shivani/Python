#5.Write a program which accept one number for user and check whether number is prime or not.


def Prime(No):

        cnt = 0
        for i in range(No):
            if(No %i== 0):
                cnt = cnt + 1
          
        if(cnt != 0):
            print(" It is Not Prime Number ")
        else:
            print(" It is Prime Number ")

def main():

    print(" Enter the Number ")
    No = int(input())

    if(No > 1):
        Prime(No)
    else:
        print(" Enter the number ")

        return 1
    
if __name__ == "__main__":
    main()
