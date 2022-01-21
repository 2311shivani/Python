#4.Write a program which accept one number form user and return addition of its factors.


def factorialadd(No):
          factorial = 0
          for i in range(No):
            if(No %i == 0):
                  factorial = factorial + i

          return factorial

def main():

    print(" Enter the Number ")
    No = int(input())

    result = factorialadd(No)
    
    print(" Addition factor of Number ", result)

if __name__ == "__main__":
    main()
