# LeetCode 23. Implement Stack using Queues

큐를 이용해 다음 연산을 지원하는 스택을 구현하라

+ puch(x) : 요소 x를 스택에 삽입한다
+ pop() : 스택의 첫 번째 요소를 삭제한다
+ top() : 스택의 첫 번째 요소를 가져온다
+ empty() : 스택이 비어 있는지 여부를 리턴한다

### [Answer 1] push()할 때 큐를 이용해 재정렬

+ _보통 스택이나 큐 ADT를 구현할 때, 스택은 연결리스트, 큐는 배열로 구현함_
+ 큐의 선언은 데크를 이용함
+ 큐를 데크로 선언했지만, 문제 의도에 맞게 큐의 연산만을 사용해 구현할 것임

```python
self.q = collection.deque()
```

+ push() 연산이 다소 복잡함
+ 요소를 삽입한 후, 방금 삽입한 요소를 맨 앞에 두는 상태로 전체를 재정렬함
    + 큐에서 맨 앞 요소를 끄집어낼 때 스택처럼 가장 먼저 삽입한 요소가 나오게 됨

```python
self.q.append()

for _ in range(len(self.q)-1):
    self.q.append(self.q.popleft())
```