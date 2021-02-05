def solution(array, commands):
    answer = []
    for index in range(len(commands)):
        command=commands[index]
        i=command[0]
        j=command[1]
        k=command[2]
        a=array[i-1:j]
        a.sort()
        x=a[k-1]
        answer.append(x)
    return answer