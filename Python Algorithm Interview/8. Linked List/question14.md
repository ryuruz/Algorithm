# LeetCode 21. Merge Two Sorted Lists
정렬되어 있는 두 연결 리스트를 합쳐라.

EX) 1->2->4 , 1->3->4 

output: 1->1->2->3->4->4


### [Answer 1] 재귀 구조로 연결

#### 1. 변수 스왑

```python
def mergeTwolists(self, l1, l2):
  if (not l1) or (l2 and (l1.val > l2.val)):
    l1, l2 = l2, l1
  if l1:
    l1.next = self.mergeTwoLists(l1.next, l2)
    
  return l1
```
l1 연결리스트에 l2 연결리스트 값을 연결하면서, 순서에 맞게 정렬하는 방식

우선 순위: __부등호__ -> __not l1__ -> __and__ -> __or__

+ l1값이 l2 값보다 크면  : if (not l1) or (l2 and (l1.val > l2.val)): 이 조건에 부합 -> l1값과 l2값을 변경

+ 해당 없으면(l1 값이 ㅣ2 보다 작으면) l1.next = self.mergeTwoLists(l1.next, l2)으로 다음 l1값 재귀함수로 설정

+ 다 끝난 후 return l1
