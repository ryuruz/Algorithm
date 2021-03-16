# LeetCode 641. Design Circular Duque

다음 연산을 제공하는 원형 데크를 디자인하라.
![IMG_1964](https://user-images.githubusercontent.com/77661701/111270163-dbfb3800-8672-11eb-88e3-434fb147fa58.jpg)


### [Answer 1] 이중 연결 리스트를 이용한 데크 구현

+ 원형 큐 구현과는 달리 맨 앞에 노드를 추가하는 insertFront() 연산 존재
  + 일반적인 배열로는 맨 앞에 요소를 추가하는 구현이 쉽지 않음 (시간복잡도 O(n))
  + 그러나 연결 리스트로는 그리 어렵지 않음

#### 1. 초기화 함수 정의
```python
def __init__(self, k):
  self.head, self.tail = ListNode(None), ListNode(None)
  self.k, self.len = k, 0
  self.head.right, self.tail.left = self.tail, self.head
```
+ 왼쪽, 오른쪽 인덱스 역할을 하는 head와 tail을 정의
+ 최대 길이 정보를 k로 설정
+ 현재 길이 정보를 담는 변수가 될 len을 self.len = 0으로 따로 정의

#### 2. 앞쪽에 노드를 추가하는 연산 : insertFront()
```python
def insertFront(self, value):
  if self.len == self.k:
    return False
  self.len += 1
  self._add(self.head, ListNode(value))
  return True
```
+ 새로운 노드를 삽입시에, 최대 길이에 도달하면 False 리턴
+ 이외에는 _add() 메서드를 이용해 head 위치에 노드 삽입

#### 3. 뒤쪽에 노드를 추가하는 연산 : insertLast()
``` python
def insertLast(self, value):
  …
  self.add_(self.tail.left, ListNode(value))
  return True
```
+ 앞쪽에 노드를 추가하는 연산과 거의 유사하지만, head가 아닌 tail.left에 삽입하는 점이 다름

#### 4. 실제 삽입을 수행하는 내부 함수 구현
내부에서만 사용한다는 의미로, PEP8 명명 규칙 기준에 따라 밑줄(_) 하나로 시작하도록 메소드 명을 _add()로 정함

```python
def _add(self, node, new):
   n = node.right
   node.right = new
   new.left, new.right = node, n
   n.left = new
```
+ 이중 연결 리스트에 신규 노드를 삽입하는 과정

![IMG_1965](https://user-images.githubusercontent.com/77661701/111270168-de5d9200-8672-11eb-8add-cdb7ff525dd0.jpg)

+ 이미 있는 노드를 찢어내고, 그 사이에 새로운 노드 new를 삽입하는 형태
+ 파란색 표기 번호 순서대로 실행

#### 5. 노드를 삭제하는 연산
```python
def deleteFront(self):
  …
  self.len -= 1
  self._del(self.head)
  
def deleteLast(self):
  …
  self.len -= 1
  self._del(self.tail.left.left)
```


