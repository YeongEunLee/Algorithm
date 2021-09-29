import sys
sys.stdin = open("input.txt", "r")

N,K = map(int,input().split())
wh = list(map(int,input().split()))
robot=[0]*N #0 N개있는 리스트 선언

res=0
#K보다 개수 작은 동안 수행
while(wh.count(0)<K):
    res+=1
    a=wh.pop()
    wh.insert(0,a)
    # pop뒤에꺼빼고 insert
    robot.pop()
    robot.insert(0,0)
    robot[N-1] = 0

    for i in range(N-2,0,-1):
        if robot[i] and wh[i+1] and (not robot[i+1]):
            robot[i]=0
            robot[i+1]=1
            wh[i+1] = max(0,wh[i+1]-1) #max와 같게
    robot[N - 1] = 0

    if wh[0] and (not robot[0]):
        robot[0]=1
        wh[0] = max(0,wh[0]-1)

print(res)