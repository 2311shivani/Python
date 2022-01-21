#1.Write a program which contains one lambda function which accepts one parameter and return power of two.

power = lambda no:no**2

def main():

    print(" Enter the number ")
    no = int(input())
    
    ret = power(no)
    
    print(" power of two numbers is = ",ret)

if __name__ == "__main__":
     main()
