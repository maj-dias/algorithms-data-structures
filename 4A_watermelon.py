def main():
    x = float(input())

    yes = False
    a=1
    b=x-1
    for i in range(int(x/2)):
        if a%2==0 and b%2==0:
            print("YES")
            yes=True
            return
        else:
            a+=1
            b-=1
    if not yes:
        print("NO")

if __name__=='__main__':
    main()