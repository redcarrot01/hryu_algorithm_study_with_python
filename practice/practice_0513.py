# def solution(numbers):
#     answer = []
#     for i in numbers:
#         b_i = bin(i)
#         temp = i + 1
#         while True:
#             b_temp = bin(temp)
#             s_i = str(b_i)
#             s_i = s_i.replace("b", "0")
#             print(s_i)
#             s_temp = str(b_temp)
#             s_temp = s_temp.replace("b", "0")
#             print(s_temp)
#             cnt = 0
#             cnt_over = 1
#             for t in range(len(s_i), -1, -1):
#                 if len(s_i) == len(s_temp) and s_i[t] != s_temp[t]:
#                     cnt += 1
#                 elif len(s_i) != len(s_temp) and s_i[t] != s_temp[t]:
#                     cnt_over += 1
#             print(cnt_over)
#             if 0 < cnt <= 2:
#                 answer.append(temp)
#                 break
#             elif 0 < cnt_over <= 2:
#                 answer.append(temp)
#                 break
#             else:
#                 temp += 1
#
#     return answer
# solution([3, 7])

from collections import deque

n, m, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

height = n
width = m
x, y = 0, 0

while True:
    if height == 0 or width == 0:
        break
    rotate(x, y, height, width)
    x += 1
    y += 1
    height -= 2
    width -= 2

for i in graph:
    for j in i:
        print(j, end=" ")
    print()


def rotate(x, y, height, width):
    # global graph
    q = deque()
    # 윗변 왼 -> 오른
    for i in range(y, y + width):
        q.append(graph[x][i])
    # 오른변 위 -> 아래
    for i in range(x + 1, x + height):
        q.append(graph[i][y + width - 1])
    # 밑변 오른 -> 왼
    for i in range(y + width - 2, y, -1):
        q.append(graph[x + height - 1][i])
    # 왼변 아래 -> 위
    for i in range(x + height - 1, x, -1):
        q.append(graph[i][y])
    q.rotate(-r)

    for i in range(y, y + width):
        graph[x][i] = q.popleft()

    for i in range(x + 1, x + height):
        graph[i][y + width - 1] = q.popleft()

    for i in range(y + width - 2, y, -1):
        graph[x + height - 1][i] = q.popleft()

    for i in range(x + height - 1, y, -1):
        graph[i][y] = q.popleft()