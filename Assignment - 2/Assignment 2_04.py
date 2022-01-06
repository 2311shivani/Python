#4.Write a program which accept one number form user and return addition of its factors.


def factorialadd(x):
          i = 1
          add = 0
          while x > i:
                    if x % i == 0:
                              add = add + i
                    i = i + 1
          return add

x = int(input(" Enter the  number "))
print(" add is ",+factorialadd(x))               


