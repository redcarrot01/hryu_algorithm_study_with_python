def solution(numbers):
    answer = []
    for i in numbers:
        b_i = bin(i)
        temp = i + 1
        while True:
            b_temp = bin(temp)
            s_i = str(b_i)
            s_i = s_i.replace("b", "0")
            print(s_i)
            s_temp = str(b_temp)
            s_temp = s_temp.replace("b", "0")
            print(s_temp)
            cnt = 0
            cnt_over = 1
            for t in range(len(s_i), -1, -1):
                if len(s_i) == len(s_temp) and s_i[t] != s_temp[t]:
                    cnt += 1
                elif len(s_i) != len(s_temp) and s_i[t] != s_temp[t]:
                    cnt_over += 1
            print(cnt_over)
            if 0 < cnt <= 2:
                answer.append(temp)
                break
            elif 0 < cnt_over <= 2:
                answer.append(temp)
                break
            else:
                temp += 1

    return answer
solution([3, 7])

