#6.Write a program which accept number from user and check whether that number is positive or negative or zero.

def printnumber(No):
        
          if (No > 0):
                    print("Number is positive")
          elif (No < 0):
                    print("Number is  negative")
          else:
                    print("Number is  zero")

def main():

    print(" Enter the  number ")
    no = int(input())

    result = printnumber(No)

if __name__ == "__main__":
    main()





        

