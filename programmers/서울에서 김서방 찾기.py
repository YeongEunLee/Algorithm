def solution(seoul):
    for i in range(len(seoul)):
        if "Kim" == seoul[i]:
            return "김서방은 "+str(i)+"에 있다"


def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))
