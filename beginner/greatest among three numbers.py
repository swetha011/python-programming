def main():
    a=raw_input("enter a")
    b=raw_input("enter b")
    c=raw_input("enter c")
    if(a>b and a>c):
        print(str(a)+"is greater")
    elif(b>a and b>c):
        print(str(b)+"is greater")
    else:
        print(str(c)+"is greater")


if __name__ == '__main__':
    main()
