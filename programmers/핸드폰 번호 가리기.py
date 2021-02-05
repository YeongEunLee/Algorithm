def solution(phone_number):
    return phone_number.replace(phone_number[:-4],'*'*(len(phone_number)-4))

# 문자열.replace("바꿔야하는 문자", "바꿀문자")
#len(문자열길이)-4 -> 4개 빼고 바꾸야하므로
#문자열[:-4] -> 뒤에 4개
# "x"*(개수) -> 개수만큼 문자열 반복