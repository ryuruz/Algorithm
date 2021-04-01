# LeetCode 332. Reconstructed Itinerary

[from, to]로 구성된 항공권 목록을 이용해 JFK에서 출발하는 여행 일정을 구성하라. 여러 일정이 있는 경우 사전 어휘 순으로 방문한다.

EX) tickets = [['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]

>> ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']

### [Answer 1] DFS로 일정 그래프 탐색
+ KEY가 출발지이고, VALUE가 도착지인 Dictionary 구성
  + Default dict 이용
+ 어휘 순으로 방문해야 하기 때문에 정렬 필요
  + sort() 이용

```python
graph = collections.defaultdict(list) # 함수 인자에 list -> value값으로 list를 가짐
for a, b in tickets:
  graph[a].append(b)
for a in graph:
  graph[a].sort() # 어휘 순 정렬을 위해 a가 가진 value들을 sorting
```

+ 매번 sort()를 하지 않고 tickets을 정렬해도 결과는 동일함
+ tickets = [['JFK','SFO'],['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]일 때,
```python
graph = collections.defaultdict(list)
for a,b in sorted(tickets): # sotrted(tickets) = [['ATL', 'JFK'], ['ATL', 'SFO'], ['JFK', 'ATL'], ['JFK', 'SFO'], ['SFO', 'ATL']]
  graph[a].append(b) # graph = {'ATL' : ['JFK', 'SFO'], 'JFK' = ['ATL', 'SFO'], 'SFO' = ['ATL']}
```
+ pop()으로 재귀 호출하며, 그래프에서 element를 꺼내 결과에 추가함

```python
def dfs(a):
  while graph[a]:
    dfs(graph[a].pop(0)) # 가장 마지막에 도착하는 도착지까지 탐색, pop호출이므로 탐색 후 삭제됨
  route.append(a)
  
return route[::-1] # 다시 뒤집어 어휘 순 결과로 출력
```
### [Answer 2] 스택 연산으로 큐 연산 최적화 시도
+ pop연산을 사용하는 경우, 인덱스가 지정되지 않은 가장 최근의 값(마지막 값)을 꺼내는 경우 O(1)이지만, 첫번째 값을 꺼내는 경우 시간 복잡도가 O(n)으로 비효율적
+ 따라서 애초부터 tickets 정렬을 역순으로 구성하여 pop() 연산 이용 
```python
for a, b in sorted(tickets, reverse = True):
  graph[a].append(b)
∙∙∙
def dfs(a):
  while graph[a]:
    dfs(graph[a].pop())
```

### [Answer 3] 일정 그래프 반복
+ 위처럼 재귀 구조가 아닌, 동일한 구조를 반복으로 풀이
+ 그래프 구성은 동일
```python
stack = ['JFK']
while stack:
  while graph[stack[-1]]: # stack의 마지막 값(마지막 도착지)가 graph에 있을 때(출발지로 존재할 때)
    stack.append(graph[stack[-1]].pop(0)) # 그 출발지의 도착지를 stack에 추가 
  route.append(stack.pop()) # 다시 거꾸로 담기기 때문에, 다시 뒤집어 어휘 순 결과로 리턴해야함 route[::-1]
```
