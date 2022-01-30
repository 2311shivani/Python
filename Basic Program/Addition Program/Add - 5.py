def Addition(Value1, Value2):
    Ans = Value1 + Value2
    return Ans

def main():
    print(" Marvellous Addition Application ")

    No1 = int(input(" Enter First Number : "))
    No2 = int(input(" Enter Second Number : "))

    ret = Addition(No1, No2);

    print(" Addition of two Numbers : ", ret);

if __name__ == "__main__":
    main();

