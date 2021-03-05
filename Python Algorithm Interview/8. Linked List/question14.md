# LeetCode 21. Merge Two Sorted Lists
정렬되어 있는 두 연결 리스트를 합쳐라.

EX) 1->2->4 , 1->3->4 

output: 1->1->2->3->4->4


### [Answer 1] 재귀 구조로 연결

#### 1. 변수 스왑
```python
if (not l1) or (l2 and l1.val > l2.val):
  l1, l2 = l2, l1
```
