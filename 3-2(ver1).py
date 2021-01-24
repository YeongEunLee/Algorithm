# N: 배열의 길이
# M: 주어진 수들을 몇번 더하는지
# K: 몇번 초과할 수 없는지

n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

sum = 0  # 결과 값 저장할 곳

while True:
    for i in range(k):  # 가장 큰 수를 K번 더하기
        if m == 0:  # m = 0일 때 반복 문 탈출
            break
        sum += data[-1]
        m -= 1
    if m == 0:  # m = 0일 때 반복 문 탈출
        break
    sum += second  # 두번째로 큰 수 한 번 더하기
    m -= 1
    # 이 문제를 푸는 알고리즘은 가장 큰 수를 만드는 것!
print(sum)
