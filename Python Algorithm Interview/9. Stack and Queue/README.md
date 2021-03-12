# 스택

+ 후입선출 처리 (LIFO)
+ 파이썬에서 별도로 스택 자료형을 제공하지는 않지만, 리스트가 사실상 스택의 모든 연산을 지원함
+ push() : 요소를 컬렉션에 추가함
+ pop() : 아직 제거되지 않은 가장 최근에 삽입된 요소를 제거함
+ 연결리스트를 활용한 스택 ADT 구현

```python
class Node: # 리스트를 담을 Node 클래스 정의
    def __init__(self, item, next):
        self.item = item # item : 노드의 값
        self.next = next # next : 다음 노드를 가리키는 포인터

class Stack:
    def __init__(self):
        self.last = None

    def push(self, item): # 연결 리스트에 요소를 추가하고 가장 마지막 값을 next로 지정. 포인터 last는 가장 마지막으로 이동시킴
        self.last = Node(item, self.last)

    def pop(self): # 가장 마지막 아이템을 끄집어내고 last 포인터를 한 칸 앞으로 전진시킴
        item = self.last.item
        self.last = self.last.next
        return item
```

# 큐

+ 선입선출 처리 (FIFO)
+ 파이썬에서 리스트로 큐의 모든 연산 지원
    + 다만 리스트는 동적 배열로 구현되어 있어, 큐의 연산을 수행하기에 효율적이지 않음
+ Deque라는 별도의 자료형을 사용하면 좋은 성능을을 냄
