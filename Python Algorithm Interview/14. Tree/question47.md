# LeetCode 297. Serialize and Deserialize Binary Tree
이진 트리를 배열로 직렬화하고, 반대로 역직렬화하는 기능을 구현하라.

### [Answer 1] 직렬화 & 역직렬화 구현
+ 이진 트리는 논리적인 데이터 구조로, 이를 파일이나 디스크에 저장하기 위해 물리적인 형태로 바꿔 주는 것을 직렬화(Serialize)라고 함 ↔ 역직렬화(Deserialize)
+ 파이썬에서는 pickle이라는 직렬화 모듈을 기본으로 제공함
#### 1. 이진힙을 배열로 표현하기
![KakaoTalk_20210502_203516873](https://user-images.githubusercontent.com/77661701/116811769-fedf9e00-ab85-11eb-8fd7-e399cda2c822.jpg)
+ 이진 힙 : 완전 이진 트리로서, 배열로 표현하기 매우 좋은 구조를 가짐
  + 높이 순서대로 순회하면, 모든 노드를 배열에 빈틈없이 배치 가능함
  + 대개 트리의 배열 표현 시에는, 계산을 편하게 하기 위해서 인덱스를 1부터 사용함
  
#### 2. 직렬화
![KakaoTalk_20210502_203908459](https://user-images.githubusercontent.com/77661701/116811864-80cfc700-ab86-11eb-9e4e-dca8c6fe5e5d.jpg)
+ BFS 탐색 결과를 배열로 표현하여, 배열만 봐도 트리의 형태를 직관적으로 떠올릴 수 있도록 구현
+ 인덱스를 1부터 시작
+ 트리에서 비어있는 노드들을 #으로 표현(노드의 값들이 문자열인데, 파이썬의 null인 None은 문자열로 만들 수 없기 때문)
+ 위 그림의 트리를 배열로 구현하면, [#, A, B, C, #, #, D, E]가 될 것임

```python
def seialize(self, root):
  queue = collection.deque([(root)])
  result = ['#'] # 0번째 인덱스 값 #
  
  while queue:
    node = queue.popleft()
    if node:
      queue.append(node.left)
      queue.append(node.right)
      
      result.append(str(node.val) # 현재 노드의 값 추가
    else
      result.append('#') # 노드가 존재하지 않으면 null값인 # 추가
      
  return ' '.join(result) # 리스트를 배열 형식으로 리턴
```

#### 3. 역직렬화
+ 문자열 형태인 입력값을 처리할 수 있도록 함
```python
def deserialize(self, data):
  nodes = data.split() # 입력값을 공백 단위로 끊어, nodes 리스트의 변수로 넣음
  
  root = TreeNode(int(nodes[1])) # 트리로 만들어줄 노드 변수 셋팅
  queue = collections.deque([root]) # 큐 변수 
```
+ 왼쪽 자식과 오른쪽 자식이 별도의 인덱스를 부여받아 큐를 순회
```python
...
  index = 2
  while queue:
    node = queue.popleft()
    if nodes[index] is not '#':
      node.left = TreeNode(int(nodes[index]))
      queue.append(node.left)
    index += 1
    
    if nodes[index] is not '#':
      node.right = TreeNode(int(nodes[index]))
      queue.append(node.right)
    index += 1
```
