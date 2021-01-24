# N: 배열의 길이
# M: 주어진 수들을 몇번 더하는지
# K: 몇번 초과할 수 없는지

n, m, k = list(map(int, input().split()))
data = list(map(int, input().split()))

data.sort()
first = data[n-1]
second = data[n-2]

# 가장 큰 수가 더해지는 횟수 계산
# 만약 주어진 수를 10번 더하는 알고리즘에서 k가 3라면
# (3 + 1) + (3 + 1) + 2(나머지) 로 총 8번 가능 !
# 따라서 m / (k+1)로 구할 수 있다.
count = int(m / (k + 1)) * k  # 몫 * K번
count += m % (k + 1)  # 나머지 더하기

sum = 0
sum += count * first  # 가장 큰 수 더하기
sum += (m - count) * second  # 두번째로 큰 수 더하기
print(sum)
