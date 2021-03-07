# LeetCode 24. Swap Nodes in Pairs
연결 리스트를 입력받아 페어 단위로 스왑하라

### [Answer 1] 값만 교환

+ 연결 리스트의 노드를 변경하는 것이 아닌 노드 구조는 그대로 유지하되 값만 변경하는 방법

+ 연결 리스트에서 사실상 값만 바꾸는 것은 비효율적 -> 빨리 풀고자하는 ,, 변칙적 방법

```python
def swapPairs(self, head):
  cur = head
  
  while cur and cur.next:
    cur.val, cur.next.val = cur.next.val, cur.val
    cur = cur.next.next
  
  return head
```

### [Answer 2] 반복 구조로 스왑

+ 1번 처럼 단순히 값만을 바꾸는 것이 아니라 연결 리스트 자체를 바꾸려면 다소 복잡함
+ prev -> head -> b 가 있을 때, 
```python
def swapPairs(self, head):
  root = prev = ListNode(None)
  prev.next = head
  
  while head and head.next:
    b = head.next
    # b가 head를 가리키도록 할당
    head.next = b.next
    b.next = head
    
    # prev가 b를 가리키도록 할당
    prev.next = b
    
    # 다음 비교를 위해 이동
    head = head.next
    prev = prev.next.next
    
  return root.next # 연결리스트의 head가 계속 바뀌는 풀이이므로, head 리턴 불가. 이전 값을 root로 설정해서 다음 root.next를 리턴하도록 함
```

### [Answer 3] 재귀 구조로 스왑
+ 재귀 구조로 풀이시, 더미노드 없이도 head를 바로 리턴 가능

```python
def swapPairs(self, head):
  if head and head.next:
    p = head.next
    
    head.next = self.swapPairs(p.next) # 재귀로 p의 다음 노드 연결
    p.next = head
    return p
    
  return head
```
