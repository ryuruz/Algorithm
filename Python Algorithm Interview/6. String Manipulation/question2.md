# LeetCode 344. Reverse String
문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.


### [Answer 1] 투 포인터를 이용한 스왑

+ 투 포인터 : 2 개의 포인터를 이용해 범위를 조정해가며 풀이하는 방식

### [Answer 2] 파이썬 다운 방식 (Pythonic way)

+ 리스트 메소드인 reverse() 이용 

#### 슬라이싱 이용

```python
# O(1)의 공간 복잡도 제한으로, 리트코드에서 오류 발생
s = s[::1]

# 트릭 이용
s[:] = s[::-1]
```
