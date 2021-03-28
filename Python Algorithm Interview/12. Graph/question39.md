# LeetCode 207. Course schedule

0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0,1] 쌍으로 표현하는 n개의 코스가 있다. 코수 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라

### [Answer 1] DFS로 순환 구조 판별
+ 순환 구조라면 계속 뱅글뱅글 맴돌게 될 것이므로, 순환구조인지 판별하는 문제로 풀이 가능함

#### 1. 순환 판별 알고리즘
+ 페어들의 목록인 prerequisites 변수를 풀어서 그래프로 표현함
```python
graph = collection.defaultdict(list)
for x,y in prerequisites:
    graph[x].append(y)
```                
+ 순환 구조를 판별하기 위해 앞서 이미 방문했던 노드를 traced 변수에 저장함

```python
traced = set() # 중복값을 갖지 않도록 set() 집합 자료형으로 정함

for x in graph:
    if not dfs(x):
        return False # 이미 방문했던 곳을 중복으로 방문하게 된다면 False 리턴 후 종료
…
return True
```

```python
def dfs(i):
    if i in traced:
        return False
    
    traced.add(i)
    for y in graph[i]:
        if not dfs(y):
            return False
    
    traced.remove(i)

    return True
``` 

### [Answer 2] 가지치기를 이용한 최적화
```python
visited = set()

def dfs(i):
    if i in traced:
        return False
    if i in visited: # 이미 한 번 방문했던 노드를 저장하기 위한 visited라는 별도의 set 변수를 생성
        return True

    return True