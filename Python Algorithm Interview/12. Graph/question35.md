# LeetCode 77. Combination

전체 수 n을 입력받아 k개의 조합은 리턴하라.

### [Answer 1] DFS로 k개의 조합 생성
+ 자기 자신과 앞에서 언급된 모든 요소를 배제하고 element를 구성함
```python
def dfs(elements, start, k):
    if k == 0:
        result.append(elements[:]) # k가 0이 되었을 때, 마지막 결과 리턴
    
    for i in range(start, n+1): # 자신 이전의 모든 값을 고정하여 재귀를 호출함
        elements.append(i)
        dfs(elements, i+1, k-1) # k를 점차 줄여나감
        elements.pop() # 해당 숫자의 조합 구성이 끝나면 요소 제거 
```
### [Answer 2] itertools 모듈 사용
```python
def combine(self, n, k):
    return list(itertools.combinations(range(i, n+1), k))
```
