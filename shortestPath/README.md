# 최단경로 알고리즘

### 최단 경로 문제

- 가장 짧은 경로 찾기
- 다양한 문제 상황
  - 한 지점에서 다른 한 지점까지의 최단 경로
  - 한 지점에서 다른 모든 지점까지의 최단 경로
  - 모든 지점에서 다른 모든 지점까지의 최단 경로
- 각 지점은 **노드로**
- 연결된 도로는 **간선으로**

### 다익스트라 최단 경로 알고리즘 개요

- **특정한 노드**에서 출발하여 **다른 모든 노드**로 가는 최단 경로를 계산
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작
  
  - 간선은 음으로 표현 안함
- 다익스트라 최단 경로 => 그리디 알고리즘 >> dp(최단경로 + 길찾기) , 그리디에 가까움
  
- **매 상황에서 가장 비용 적은 노드 선택하여 반복**
  
  #### 알고리즘의 동작 과정
  
  1. 출발 노드를 설정
  2. 최단 거리 테이블 초기화
  3. 방문하지 않은 노드 중 최단거리가 짧은 노드 선택 (그리디)
  4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산하여 최단 거리 테이블 갱신
  5. 3, 4반복
  

### 다익스트라 알고리즘 동작 과정 자세히

- 더 짧은 경로 찾으면 최단 거리 테이블 갱신

![image](https://user-images.githubusercontent.com/38436013/114259351-49974b80-9a08-11eb-9422-2c8b439aec7e.png)

![image](https://user-images.githubusercontent.com/38436013/108315540-e571bb80-71fe-11eb-99ed-42f754b8587c.png)
![image](https://user-images.githubusercontent.com/38436013/108315554-ec98c980-71fe-11eb-8276-ad6829418ad4.png)
![image](https://user-images.githubusercontent.com/38436013/108315573-f3274100-71fe-11eb-8dde-d6b4db0300be.png)

![image](https://user-images.githubusercontent.com/38436013/114259384-7cd9da80-9a08-11eb-9cc7-536959b1198c.png)
![image](https://user-images.githubusercontent.com/38436013/114259385-85caac00-9a08-11eb-8fac-e0edc42803e7.png)
![image](https://user-images.githubusercontent.com/38436013/114259390-8d8a5080-9a08-11eb-8b65-3192396c7e42.png)

### 다익스트라 알고리즘 특징

- 그리디 알고리즘 : 매상황에서 방문하지 않은 가장 비용이 적은 노드 선택
- 단계 거치며 **한번 처리된 노드(이미 방문 처리)의 최단 거리는 고정**되어 바뀌지 않음
  - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해
- 다익스트라 수행 후 , 테이블에 각 노드까지의 최단 거리 정보가 저장됨
- 단계마다 방문하지 않은 노드 중 최단 거리 가장 짧은 노드 선택하기 위해 **매 단계마다 1차원 테이블의 모든 원소를 확인(순차 탐색)**

### 간단한 다익스트라 구현

~~~
# 노드 개수, 간선 개수
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())


INF = int(1e9) # 10억
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)] # [[], [], ...]
# 방문한 적이 있는지 체크하는 목적의 리스트를 만들기
visited = [False] * ( n + 1) 
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c
    graph[a].append((b, c))
#print(graph)    
# [[], [(2, 2), (3, 5), (4, 1)], [(3, 3), (4, 2)], [(2, 3), (6, 5)], 
# [(3, 3), (5, 1)], [(3, 1), (6, 2)], []]   

# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스) 
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
        #print(distance[j[0]])  2 5 1
        
    # 시작 노드를 제외한 전체 n -1 개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드 꺼내서 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                
            
# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])     
~~~

### 간단한 구현 방법 성능 분석

- 순차 탐색 : 시간복잡도 O(N^2)
- O(N)번에 걸쳐서 최단거리가 가장 짧은 노드 매번 선형탐색해야 하고, 현재 노드와 연결된 노드 매번 확인
- 전체노드개수가 5000이하라면 이렇게 풀 수 있으나 10000개넘어가면 해결 어려움

---

---

### 우선순위 큐

- 우선순위 가장 높은 데이터 가장 먼저 삭제하는 자료구조

### 힙

- 우선순위 큐 구현하기 위해 사용하는 자료구조 중 하나

- 최소 힙과 최대 힙이 있음

- 데이터 삽입, 삭제가 빠른편이다

- 내부적으로 트리구조이므로, 시간복잡도 logN만큼 수행한다.

  | 우선순위 큐 구현 방식 | 삽입 시간 | 삭제 시간 |
  | --------------------- | --------- | --------- |
  | 리스트                | O(1)      | O(N)      |
  | 힙                    | O(logN)   | O(logN)   |

### 개선된 다익스트라

- 힙 자료구조 사용
- 다익스트라 알고리즘이 동작하는 기본원리는 동일
  - 현재 가장 가까운 노드를 저장해 놓기 위해서 힙을 추가적으로 사용
  - 현재의 최단거리가 가장 짧은 노드 선택해야 하므로 최소 힙 사용

### 우선순위 큐 이용한 다익스트라 동작 과정

![image](https://user-images.githubusercontent.com/38436013/114259563-c2e36e00-9a09-11eb-8421-3684e5723040.png)
![image](https://user-images.githubusercontent.com/38436013/114259498-494b8000-9a09-11eb-8747-0a017d8b6af8.png)
![image](https://user-images.githubusercontent.com/38436013/114259501-51a3bb00-9a09-11eb-8ca6-439825a1ce77.png)
![image](https://user-images.githubusercontent.com/38436013/114259505-59fbf600-9a09-11eb-8e04-c50b3f3b287d.png)
![image](https://user-images.githubusercontent.com/38436013/114259510-63855e00-9a09-11eb-80d4-5ec8ddab2dcb.png)
![image](https://user-images.githubusercontent.com/38436013/114259515-6aac6c00-9a09-11eb-8788-50c41413c8ed.png)
![image](https://user-images.githubusercontent.com/38436013/114259567-cd056c80-9a09-11eb-85e5-ff932d97ac4b.png)
![image](https://user-images.githubusercontent.com/38436013/114259529-7dbf3c00-9a09-11eb-87f7-be2f0ddb8ab9.png)
![image](https://user-images.githubusercontent.com/38436013/114259570-d4c51100-9a09-11eb-9e9f-d8f407164bed.png)

### 개선된 다익스트라 구현

~~~
import heapq
# import sys
# input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수 
n,m = map(int, input().split())
# 시작 노드 번호 
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보 담는 리스트 만들기
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 련재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:# i[0] : 도착 노드임 , 햇갈리지 말자
                distance[i[0]]= cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한 이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])
~~~

### 개선된 구현 방법 성능 분석

- V : 노드 , E : 간선

- 힙 자료구조 이용하는 다익스트라 알고리즘의 시간복잡도는 O(ElogV)
- 노드를 하나씩 꺼내 검사하는 반복문은 노드의 개수 V 이상의 횟수로는 처리되지 않음
  - 결과적으로 현재 우선순위 큐에서 꺼낸 노드와 연결된 다른 노드들을 확인하는 총횟수는 최대 간선의 개수(E)만큼 연산이 수행될 수 있음(내부적으로 힙이 정렬해주기 때문에 )
- 직관적으로 전체 과정은 E개의 원소를 우선순위 큐에 넣었다가 모두 빼내는 연산과 매우 유사
  - 시간복잡도를  O(ElogE)로 판단 가능
  - 중복 간선(양방향) 포함하지 않는 경우, 이를  O(ElogV)로 정리
    - O(ElogE) -> O(ElogV^2) -> O(2ElogV) -> O(ElogV) ( 앞에 곱해진 2는 표기법에서 제거 )
    - 간선 개수 100,000개 , 노드 개수 10000개 까지는 1초안에 해결

---

---

### 플로이드 와샬 알고리즘

- 모든 노드에서 다른 모든 노드까지의 최단 경로
- 다익스트라와 마찬가지로 단계별로 거쳐 가는 노드를 기준으로 알고리즘 수행
  
  - 다만 매 단계마다 방문하지 않은 노드 중에 최단 거리를 갖는 노드를 찾는 과정 필요x
- 2차원 테이블에 최단 거리 정보 저장
- DP에 속함 (2차원 테이블의 값을 점화식에 따라 처리하므로 dp임)

- 각 단계마다 특정 노드 K 거쳐 가는 경우 확인

  - A -> B로 가는 최단 거리보다 A에서 K를 거쳐 B로 가는 거리가 더 짧은지
  - Dab = min(Dab, Dak+ Dkb)

  ![image](https://user-images.githubusercontent.com/38436013/108847878-a048f180-7623-11eb-8fb5-418f06245c25.png)

  ​        ![image](https://user-images.githubusercontent.com/38436013/108848059-dd14e880-7623-11eb-82c8-6e13b9f9dd1e.png)

- 플로이드 워셜을 사용하는 문제는 노드의 개수가 500개 이하인 경우 대부분 -> 시간복잡도가 n*n *n 이므로 n=1000이라면 10억을 넘어간다

### 플로이드 워셜 구현

~~~
INF = int(1e9) # 무한을 의미하는 10억 설정

# 노드의 개수 및 간선의 개수 입력 받기
n = int(input())
m = int(input())
# 2차원 리스트를 만들고, 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a==b:
            graph[a][b] = 0
# 각 간선에 대한 정보 입력받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c
    
# 점화식에 따라 플로이드 워셜 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+ graph[k][b])

# 수행된 결과 출력
for a in range(1, n+1):
    for b in range(1, n+1):
        # 도달할 수 없는 경우, 무한으로 출력
        if graph[a][b] == INF:
            print("INFINITY", end= ' ')
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(graph[a][b], end=' ')
        print()
~~~

### 플로이드 워셜 알고리즘 성능 분석

- 노드의 개수가 N개일 때 알고리즘상으로 N번의 단계를 수행
  - 각 단계마다 O(N^2)의 연산을 통해 현재 노드를 거쳐 가는 모든 경로를 고려
  - 총 시간 복잡도는 0(N^3)