#8. Write a program which accept one number and display below pattern.

def PrintPattern(No):
          for i in range(1, No +1):
                for j in range(1, No +1):
                    if(i >= j):
                              print(j,end=" ")
                             
                print(" \n ")

def main():
    
    print(" Enter the Number ")
    No = int(input())

    PrintPattern(No)

if __name__ == "__main__":
    main()
