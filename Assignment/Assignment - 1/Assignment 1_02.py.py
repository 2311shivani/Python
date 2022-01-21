#2.Write a program which contains one function named as ChkNum() which accept one parameter as number. If number is even then it should display Even number otherwise display Odd number on console.

def chkNum():
    if(num % 2)==0:

          print("Enter a Even Number :");
    else:
          print("Enter a Odd Number :");

def main():
         
        print("Enter a number :")
        num = int(input())

        Ret = chkNum()
        
if __name__ == "__main__":
    main()
