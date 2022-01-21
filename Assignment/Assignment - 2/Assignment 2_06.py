#6. Write a program which accept one number and display below pattern.


def printpattern(No):
    
          for i in range(No, 0, -1):
                for j in range(0, i):
                              print(" * ", end = " ")
                            
                print(" \n ")

def main():

    print(" Enter the number ")
    No = int(input())

    printpattern(No) 

if __name__ == "__main__":
    main()
