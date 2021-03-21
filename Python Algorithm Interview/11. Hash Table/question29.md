# LeetCode 771. Jewels and Stones

J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.

### [Answer 1] 해시 테이블을 이용한 풀이

+ 갖고있는 돌 s의 원소 개수를 모두 헤아린 후, J에서 각 요소를 키로 가지는 수를 합산하여 풀이

#### 1. 돌 빈도 수 계산
```python
freqs = {} # 해시 테이블 정의

for char in S:
    if char not in freqs: # freqs에 없으면 추가
        freqs[char] = 1
    else: # 존재하면 빈도수 1 추가
        freqs[char] += 1

```
#### 2. 보석 빈도 합산
```python
for char in J:
    if char in freqs:
        count += freqs[char]

return count
```

### [Answer 2] 딕셔너리 이용
```python
# defaultdict 이용
for char in S:
    freqs[char] += 1

for char in J:
    count += freqs[char]

return count
```

### [Answer 3] Counter 이용
+ element에 대한 개수를 계산해 딕셔너리로 리턴
```python
freqs = collections.Counter(S)
count = 0
for char in J:
    count += freq[char]
```

### [Answer 4] 한 줄 풀이

```python
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum(s in J for s in S)
```
