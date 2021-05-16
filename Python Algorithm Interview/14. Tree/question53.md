# LeetCode 783. Minimum Distance Between BST Nodes
두 노드 간 값의 차이가 가자 작은 노드의 값의 차이를 출력하라.

### [Answer 1] 재귀 구조로 중위 순회
+ 이진 탐색 트리 (BST) : 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이루어져 있고, 오른쪽 서브트리에는 그 노드의 값과 같거나 큰 값들을 지닌 노드들로 이루어진 트리
  + BST의 왼쪽 자식은 항상 루트보다 작고, 오른쪽 자식은 항상 루트보다 크다는 점 유의  
#### 1. 중위 순회
```python
def f():
  if root.left:
    f(root.left)
    
  result = min()
  
  if root.right:
    f(root.right)
```

### [Answer 2] 반복 구조로 중위 순회
+ 재귀보다 훨씬 직관적

