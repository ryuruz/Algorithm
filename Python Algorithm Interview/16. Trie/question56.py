# LeetCode 208. Implement Trie (Prefix Tree)
트라이의 insert, search, startsWith 메소드를 구현하라
+ search : 단어 존재 여부 판별
+ startsWith : 해당 문자열로 시작하는 단어가 존재하는지 여부 판별

### [Answer 1] 딕셔너리를 이용해 간결한 트라이 구현
+ 이진 탐색 트리 (BST) : 노드의 왼쪽 서브트리에는 그 노드의 값보다 작은 값들을 지닌 노드들로 이루어져 있고, 오른쪽 서브트리에는 그 노드의 값과 같거나 큰 값들을 지닌 노드들로 이루어진 트리
  + BST의 왼쪽 자식은 항상 루트보다 작고, 오른쪽 자식은 항상 루트보다 크다는 점 유의  
#### 1.  트라이 선언
```python
class TrieNode:
  def __init__(self):
    self.word = False
    self.children = {}
```
#### 2. 트라이 연산 구현
```python
class Trie:
  def __init__(self):
    self.root = TrieNode()
  
  # Insert  
  def insert(self, word):
    node = self.root
    for char in word:
      if char not in node.children:
        node.children[char] = TrieNode()
        # self.children을 default.dict()으로 선언하여 간결하게 표현 가능
        # Trie 선언 시 self.children = collection.defaultdict(TrieNode)
        # 위 코드 대신 node = node.children[char]
      node = node.children[char]
      
    node.word = True
```

##### Search
```python
def search(self, word):
  node = self.root
  for char in word: # for문 순회하며 자식 노드를 타고 계속 내려가다가 여부 판별
    if char not in node.children:
      return False
    node = node.children[char]
    
  return node.word
```

###### StartsWith
```python
def startsWith(self, prefix):
  node = self.root
  fot char in prefix:
    if char not in node.children: # 자식 노드의 존재 여부 판별 
      return False
    node = node.children[char]
  
  return True
```

#### 3. 딕셔너리 이용
+ self.children을 default.dict()으로 선언하여 
