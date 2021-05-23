# LeetCode 56. Merge Interval
겹치는 구간을 병합하라

### [Answer 1] 정렬하여 병합

#### 1.  정렬
+ 파이썬 내장함수 sorted 
+ sorted(데이터, key 값)
  + 오름차순이 디폴트 (reverse = false)
  + 내름차순 reverse = true

```python
sorted(intervals, key = lambda x: x[0])
```
+ 첫 번째 값을 키로 하여, 정렬함 <-> 두 번째 값 x[1]

#### 2. 병합
```python
def merge(intervals):
  merged = []
  for i in sorted(intervals, key = lambda x: x[0]): # 정렬한 후에 
    if merged and i[0] <= merged[-1][1]: # 현재 아이템 시작이 이전 아이템의 끝과 구간이 겹치면
      merged[-1][1] = max(merged[-1][1], i[1]) # 둘 중 범위의 끝 값이 더 큰 값을 이전 아이템에 대입
    else: # 구간이 겹치지 않으면
      merged += i, # 콤마 연산자, 병합을 멈추고 새로운 아이템으로 추가
      
  return merged
```

+ 콤마 연산자 : 중첩 리스트를 만들어주는 역할
  + ex) a = [1], b = [2,3] 일 때, a += b, 는 a += [b]와 같다. 
  + a = [1, [2,3]]
