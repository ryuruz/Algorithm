# LeetCode 787. Cheapest Flights Within K stops
시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, k개의 경유지 이내에 도착하는 가격을 리턴하라. 경로가 존재하지 않을 경우 -1을 리턴한다.

### [Answer 1] 다익스트라 알고리즘 응용
+ 순환 구조라면 계속 뱅글뱅글 맴돌게 될 것이므로, 순환구조인지 판별하는 문제로 풀이 가능함

#### 1. 우선순위 큐 적용
+ 우선순위 큐를 최소 힙(mini heap)으로 구현한 모듈인 heapq를 사용
+ 우선순위 큐 : FIFO 구조인 큐와 다르게, 들어간 순서와 관계 없이 우선 순위가 높은 데이터가 먼저 나오는 구조
    + 힙(heap)을 이용하여 구현 
        + 완전 이진트리
        + 직접 연결된 자식-부모 노드간의 크기만 비교하면 됨
        + 최대 힙 (Max Heap) : 루트 노드로 올라갈수록 저장된 값이 커지는 구조, 값이 큰 순서대로 우선순위를 가짐
        + __최소 힙 (Mini Heap): 루트 노드로 올라갈수록 값이 작아지는 구조, 값이 작은 순서대로 우선순위를 가짐__

#### 2. 구현

```python
def findCheapestPrice(n, flights, src, dsc, K):
    graph = collections.defaultdic(list)
    for u, v, w in flights: # flight = [[출발지 u, 도착지 v, 가격 w], ]
        graph[u].append((v,w))

    # 큐 변수
    Q = [(0, src, K)] # 가격, 시작점, 제한된 경유지 개수

    while Q:
        price, node, k = heapq.heappop(Q)
        if node == dst: # 시작점 == 도착점, 즉 도착점에 도달했다면
            return price # 최종 price 리턴

        if k >= 0 : # 문제에서 제시된 경유지 수 이하로 유지
            for v, w in graph[node]:
                alt = price + w # 기존 가격에 경유지 가격 추가 
                heapq.heappush(Q, (alt, v, k-1)) # Q에 업데이트 값 추가, k-1 : 경유지가 하나 증가했으므로
    
    return -1 # 위 조건 만족 못하면 -1 리턴
```