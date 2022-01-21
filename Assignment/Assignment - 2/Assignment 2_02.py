#2.Write a program which accept one number and display below pattern.

def PrintPattern(No):
    
          for i in range(No):
                    for j in range(No):
                              print(" * ", end = "  ")
                              
                    print( " \n ")

def main():

    print(" Enter the  number ")
    No = int(input())
    
    PrintPattern(No)

if __name__ == "__main__":
    main()
