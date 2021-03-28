# 그래프
+ 객체의 일부 쌍(Pair)들이 연관되어 있는 객체 집합 구조
  + 정점(Vertex) : 데이터가 저장되는 부분 = 노드(Node)
  + 간선(Edge) : 노드간의 관계를 나타내는 선
  + 인접 정점(Adjacent vertex) : 간선에 의해 연결된 정점
  + 단순 경로(Simple-path) : 경로 중 반복되는 정점이 없는 경로
  + 차수(Degree) : 무방향 그래프엣 하나의 정점에 인접한 정점의 수 
## 오일러 경로
+ 오일러 정리 : 모든 정점이 짝수 개의 차수를 갖는다면, 모든 다리를 한 번씩만 건너서 도달하는 것이 성립함 
+ __모든 간선을 한 번씩 방문하는 유한 그래프__
## 해밀턴 경로
+ 각 정점을 한 번씩 방문하는 무향 또는 유항 그래프 경로
+ 오일러 경로와의 차이점 : 오일러 경로는 간선 기준이며, 해밀턴 경로는 정점 기준임
+ 해밀턴 경로를 찾는 문제는 최적 알고리즘이 없는 대표적인 NP-완전 문제임
+ 해밀턴 순환 : 원래의 출발점으로 돌아오는 경로
  + 해밀턴 순환의 최단 거리를 찾는 문제  ex) 외판원 문제(TSP)
____
## 그래프 순회 (Graph Traversals)
+ 그래프 탐색
+ 그래의 각 정점을 방문하는 과정
### 깊이 우선 탐색 (Depth-FIrst Search)
+ 주로 쓰이는 탐색 방법
+ 주로 스택이나 재귀로 구현
+ 재귀 구조로 구현
  + 정점 v의 모든 인접 유향 간선들을 반복
  + 방문했던 정점인 discovered를 계속 누적된 결과로 만들기 위해 리턴형태를 받아옴
```python
def recursive_dfs(v, discoverd = []):
    discovered.append(v)
    for w in graph[v]:
        if not w in discovered:
            discovered = recursive_dfs(w, discovered)
    return discovered
```  
+ 스택 구조로 구현
  + 스택을 이용해 모든 인접 간선을 추출하고 다시 도착점인 정점을 스택에 삽입하는 구조로 표현
```python
def iterative_dfs(strat_v):
    discovered = []
    stack = [start_v]
    while stack:
        v = stack.pop()
        if v not in discovered:
            discovered.append(v)
            for w in graph[v]:
                stack.append(w)
    return discovered
```
### 너비 우선 탐색 (Breadth-First Search)
+ 주로 큐로 구현
+ 그래프의 최단 경로를 구하는 문제 등에 사용됨
+ 큐를 이용한 구현
    + 리스트 자료형을 사용하지만, pop(0)과 같은 큐의 연산만을 사용함
+ 재귀로 풀이할 수 없음
```python
def iterative_bfs(start_v):
    discovered = [start_v]
    queue = [start_v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in discoveredd:
                discovered.append(w)
                queue.append(w)
    return discovered
```
___
## 백트래킹(Backtracking)
+ 해결책에 대한 후보를 구축해 나아가다, 가능성이 없다고 판단되는 즉시 후보를 포기(백트랙)해 정답을 찾아가는 범용적인 알고리즘
+ 제약 충족 문제에 특히 유용함
  
## 제약 충족 문제(Constraint Satisfaction Problems)
+ 수많은 제약 조건을 충족하는 상태를 찾아내는 수하 문제

  
