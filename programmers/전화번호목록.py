#시간초과뜸..
from itertools import combinations
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in list(combinations(phone_book, 2)):
        if p2.startswith(p1):
            return False
    return True

#고친풀이
#itertools를 쓰면 왜 시간초과가 나올까..
def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True