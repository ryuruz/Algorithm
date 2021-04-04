# LeetCode 687. Longest Univalue Path
동일한 값을 지닌 가장 긴 경로를 찾아라

### [Answer 1] 상태값 거리 계산 DFS
+ 리프 노드까지 DFS로 탐색하여 내려간 다음, 값의 일치여부를 파악하며 백트리킹하는 형태로 풀이
  
#### 1. DFS 재귀 탐색
```python
def dfs(node):
    …
    left = dfs(node.left)
    right = dfs(node.right)
```
+ 리프 노드에 도착하면, 값 리턴
```python
if node is None:
    return 0
```
+ 자식 노드와 동일한 값인지 확인하는 과정
+ 왼쪽과 오른쪽 자식 노드를 각각 확인하여, 동일한 경우 거리를 1씩 증가시킴
```python
if node.left and node.left.val == node.val:
    left += 1
else:
    left = 0
if node.right and node.right.val == node.val:
    right += 1
else:
    right = 0

# 왼쪽 자식과 오른쪽 자식 노드 간 거리의 합을 결과로 함
result = max(result, left+right)
```
+ 현재 노드의 부모노드에 현재까지의 거리를 리턴
```python
return max(left, right) # 부모 노드는 현 노드의 자식 노드의 양쪽 모두를 동시에 연결할 수 없음 -> 최대값 선택
```