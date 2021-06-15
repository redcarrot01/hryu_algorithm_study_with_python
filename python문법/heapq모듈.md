## Goal

> - 우선순위 큐를 위하여 만들어진 자료구조 , 힙!
> - 우선순위큐 : 큐와 달리, 데이터 제거될때 **가장 작은 값(우선순위 높은)**을 제거하는 자료구조
> - 힙의 사용법

## 들어가기 전

![image](https://user-images.githubusercontent.com/38436013/112562262-49009180-8e1a-11eb-990e-7156861906e6.png)

## heapq 모듈 요약

- 완전이진트리 기본으로한 자료구조
- 힙의 특성 : 부모-자식 노드의 키값 대소 관계가 일정하게 유지됨
- 최대 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 큰 힙
- 최소 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 항상 작은 힙


- 파이썬에서 힙큐 모델은 최소 힙 제공
~~~
import heapq

heap = [] # 힙생성 및 초기화

# 힙원소 추가 
heap.heappush() 

# 힙원소 삭제 : 최소 힙에서는 가장 작은 값이 맨위, 맨위 원소 삭제+트리재배치
heap.heappop()

# 기존 리스트를 힙으로 만들기
list = [4,1,7]
heapq.heapify(list)
~~~

## 힙 자료구조

- 이진트리 기반의 우선순위큐를 위하여 만들어진 최소 힙 자료구조

- **최댓값 최솟값 찾는 연산 할때 사용**

- min heap을 사용하면, 

  - 원소들이 항상 정렬된 상태(? 일부가)로 추가되고 삭제되며, 
  - min heap에서 가장 작은값은 언제나 인덱스0, 
  - min heap 내의 모든 원소는 항상 자식 원소들(2k+1, 2k+2)보다 작거나 같도록 원소 추가되거나 삭제됨

  - 힙트리에서는 중복된 값 허용

~~~
heap[k] <= heap[2*k+1] and heap[k] <= heap[2*k+2]

     1  ---> root
   /   \
  3     5
 / \   /
4   8 7
~~~

![image](https://user-images.githubusercontent.com/38436013/110625229-83dfb400-81e2-11eb-8333-5441e236916f.png)

-  키값의 대소 관계는 부모/자식 간에만 성립하고, 형제노드 사이에는 대소 관계가 정해지지 않는다.

## 모듈 임포트

~~~
import heapq
~~~

## 최소 힙 생성

~~~
heap = []
~~~

## 힙에 원소 추가

~~~
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)
print(heap)

[1, 3, 7, 4]
~~~

- 가장 작은 1이 인덱스 0에 위치하며, 인덱스 1(= k)에 위치한 3은 인덱스 3(= 2k + 1)에 위치한 4보다 크므로 힙의 공식을 만족
- O(logN)의 시간 복잡도

## 힙에 원소 삭제

- heappop() 가장 작은 원소를 삭제 후 리턴

~~~
print(heapq.heappop(heap))
print(heap)

1
[3, 4, 7]
~~~

## 최소값 삭제하지 않고 얻기

~~~
print(heap[0])
4
~~~

- 주의 : 두번째 작은 원소 얻으려면 heap[1] x
- heappop() 통해 첫번째 작은 원소 지우고 heap[0]을 통해 새로운 최솟값 접근


## 기존 리스트를 힙으로 변환

~~~
heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)
print(heap)


[1, 3, 5, 4, 8, 7]
~~~

## 최대 힙

~~~
import heapq

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
  heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

while heap:
  print(heapq.heappop(heap)[1])  # index 1
  
  8
  7
  5
  4
  3
  1
~~~

- 각 값에 대한 우선 순위를 구한 후, `(우선 순위, 값)` 구조의 튜플(tuple)을 힙에 추가하거나 삭제
- 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됨 (우선 순위에는 관심이 없으므로 )

## heapq모듈 이용한 최댓값 최솟값

- `heapq.nlargest`(*n*, *iterable*, *key=None*)  : 내림차순으로 n개

- `heapq.nsmallest`(*n*, *iterable*, *key=None*) : 오름차순으로 n개

  

~~~
import heapq

nums = [1, 8, 3, -5, 4, 99, -4, 0]

print(heapq.nlargest(3, nums)) 
#> [99, 8, 4]
print(heapq.nsmallest(3, nums))
#> [-5, -4, 0]
~~~

~~~
grades = [
    {'name': 'Steve', 'grade': 80},
    {'name': 'David', 'grade': 90},
    {'name': 'Tony', 'grade': 40},
    {'name': 'Grace', 'grade': 100}
]

print(heapq.nlargest(2, grades, lambda s: s['grade'])) 
#> [Grace, David]
print(heapq.nsmallest(2, grades, lambda s: s['grade'])) 
#-> [Tony, Steve]
~~~



## k번째 최솟값 최댓값

- 최소 힙이나 최대 힙 사용
- 배열로 힙 만든 후, heapop()함수로 k번 호출

~~~
import heapq

def kth_smallest(nums, k):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)

  kth_min = None
  for _ in range(k):
    kth_min = heapq.heappop(heap)
  return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))

4(3번째 작은 값)
~~~

## 힙 정렬

~~~
import heapq

def heap_sort(nums):
  heap = []
  for num in nums:
    heapq.heappush(heap, num)
  
  sorted_nums = []
  while heap:
    sorted_nums.append(heapq.heappop(heap))
  return sorted_nums

print(heap_sort([4, 1, 7, 3, 8, 5]))



[1, 3, 4, 5, 7, 8]
~~~











