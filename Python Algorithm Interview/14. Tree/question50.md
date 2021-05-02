# LeetCode 108. Convert Sorted Array to Binary Search Tree
오름차순으로 정렬된 배열을 높이 균형 이진 탐색 트리로 변환하라.
+ 높이 균형(Height Balance) : 노든 노드의 두 서브 트리 간 깊이 차이가 1 이하인 경우

### [Answer 1] 이진 검색 결과로 트리 구성 
+ 이진 탐색 트리 (BST) : 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이루어져 있고, 오른쪽 서브트리에는 그 노드의 값과 같거나 큰 값들을 지닌 노드들로 이루어진 트리
#### 1. 재귀 이용  
```python
def sortedArrayToBST(self, nums):
  mid = len(nums) // 2 # 정확히 중앙값을 갖도록 내림값을 리턴하는 연산자 //
  
  node = TreeNode(nums[mid])
  node.left = self.sortedArrayToBST(nums[:mid]) # 왼쪽 자식 노드
  node.right = self.sortedArrayToBST(nums[mid+1:]) # 오른쪽 자식 노드
  
  return node
```
