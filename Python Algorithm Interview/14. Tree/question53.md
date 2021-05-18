# LeetCode 783. Minimum Distance Between BST Nodes
두 노드 간 값의 차이가 가장 작은 노드의 값의 차이를 출력하라.

### [Answer 1] 재귀 구조로 중위 순회
+ 이진 탐색 트리 (BST) : 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이루어져 있고, 오른쪽 서브트리에는 그 노드의 값과 같거나 큰 값들을 지닌 노드들로 이루어진 트리
  + BST의 왼쪽 자식은 항상 루트보다 작고, 오른쪽 자식은 항상 루트보다 크다는 점 유의  
#### 1. 중위 순회
+ 중위 순회 : 왼쪽 하위 트리부터 방문하여 루트 노드를 거치면서 순회
```python
# 초기 비교대상 설정
prev = -sys.maxsize # 최소 정수
result = sys.maxsize # 최대 정수

def minDiffInBST(self, root):
  if root.left:
    self.minDiffInBST(root.left)
    
  self.result = min(self.result, root.val - self.prev)
  self.prev = root.val
  
  if root.right:
    self.minDiffInBST(root.right)
    
  
  return self.result

```

### [Answer 2] 반복 구조로 중위 순회
+ 재귀보다 훨씬 직관적
+ 함수 내에서 prev, result를 선언 가능함
```python
def minDiffInBST(self, root):
  prev = -sys.maxsize
  result = sys.maxsize
  
  stack = []
  node = root
  
  # 반복
  while stack or node:
    while node:
      stack.append(node)
      node = node.left
    
    node = stack.pop()
    
    result = min(result, node.val - prev)
    prev = node.val
    
    node = node.right
    
  return result
