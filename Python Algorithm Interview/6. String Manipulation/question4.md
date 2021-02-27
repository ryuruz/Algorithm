# LeetCode 819. Most Common word 
금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다. 


### [Answer 1] 리스트 컴프리헨션, Counter 객체 사용

입력값에는 대소문자, 쉼표 등 구두점이 존재하므로 데이터 클렌징(Data Cleansing)으로 데이터 전처리가 필요하다.


+ 편하게 처리하기 위해서 정규식을 사용한다.

```python
# 단어가 아닌 모든 문자를 공백으로 치환
# banned에 포함되지 않은 단어를 대상으로 진행

words = [word for word in re.sub(r'[^\w], '', paragraph).lower().split()
  if word not in banned]
```

+ 소문자, 구두점, banned를 제외한 던어 목록의 개수를 헤아림

+ 딕셔너리를 활용하여 단어의 개수 파악

```python
# defaultdic을 활용하여, 자동으로 int형의 value를 부여한다.

counts = collections.defaultdic(int)
for word in words:
  counts[word] += 1
```

+ get(x) : x(key)에 대응되는 value를 리턴하는 함수 

```python
# 딕셔너리에서 값이 가장 큰 키를 불러온다.

return max(counts, key = count.get)
```

+ 가장 흔하게 등장하는 단어를 추출함
_ex) [('A',3)]일 경우, 첫 번째 인덱스인 A를 출력하도록 함_

```python
counts = collections.Counter(words)
return counts.most_common(1)[0][0] #최다 빈도 요소 추출 : most_common(몇 개의 요소를 추출할건지)
```
