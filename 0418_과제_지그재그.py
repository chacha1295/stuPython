def main():

    num = int(input("정수를 입력하시오. : "))
    vlist = [[ 0 for _ in range(num)] for _ in range(num)] #배열0으로 초기화


    a=1
    b=0
    val=2 #배열에 입력될 수
    n = 1 #적재 횟수 및 배열 개수
    if num%2==1: #입력받은 수가 홀수 일 경우
        for _ in range(0,num-1): # list[0][0]을 제외하기 위해 -1번 돌린다.
            #대각선으로 절반부분 까지 적재하는 부분이다.
            n=n+1     #처음에 2번 적재 하고, 끝날때 입력받은 수만큼 적재하기 위해
            if n%2==0:    #적재 횟수가 짝수일 때는 선입력, 후 계산
                for _ in range(0,n):
                    vlist[a][b]=val
                    val=val+1
                    if a==0: #a를 -1로 하는데
                        b=b+1
                    else:
                        a=a-1
                        b=b+1
            elif n%2==1: #적재 횟수가 홀수일 때
                for _ in range(0,n):
                    vlist[a][b]=val
                    val=val+1
                    if b==0:
                        a=a+1
                    else:
                        a=a+1
                        b=b-1


        for _ in range(0,num-1):
            n=n-1

            if n%2==0:
                for _ in range(0,n):
                    a=a-1
                    b=b+1
                    print("s a = ",a)
                    print("S b = ",b)
                    vlist[a][b]=val
                    val=val+1
                a=a+1

            elif n%2==1:
                for _ in range(0,n):
                    print("s2 a = ",a)
                    print("s2 b = ",b)
                    vlist[a][b]=val
                    val=val+1
                    a=a+1
                    b=b-1
                b=b+1
        vlist[0][0]=1
        vlist[num-1][num-1]=num*num



    if num % 2 == 0:
        for _ in range(0, num - 1):
            n = n + 1
            if n % 2 == 0:
                for _ in range(0, n):
                    vlist[a][b] = val
                    val = val + 1
                    if a == 0:
                        b = b + 1
                    else:
                        a = a - 1
                        b = b + 1
            elif n % 2 == 1:
                for _ in range(0, n):
                    vlist[a][b] = val
                    val = val + 1
                    if b == 0:
                        a = a + 1
                    else:
                        a = a + 1
                        b = b - 1

        for _ in range(0, num - 1):
            n = n - 1

            if n % 2 == 0:
                for _ in range(0, n):
                    vlist[a][b] = val
                    a = a - 1
                    b = b + 1
                    val = val + 1
                a = a + 1

            elif n % 2 == 1:
                for _ in range(0, n):
                    a = a + 1
                    b = b - 1
                    vlist[a][b] = val
                    val = val + 1
                b = b + 1



    vlist[0][0] = 1
    print("vlist=", vlist[0])
    print("vlist=", vlist[1])
    print("vlist=", vlist[2])
    print("vlist=", vlist[3])
    print("vlist=", vlist[4])
    print("vlist=", vlist[5])
    # print("vlist=", vlist[6])


if __name__ == "__main__":
    main()