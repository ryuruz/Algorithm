# LeetCode 125. Valid Palindrome
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.

# 팰린드롬 (Palindrome)
- 앞 뒤가 똑같은 단어나 문장으로 뒤집어도 같은 말이 되는 단어 또는 문장
- 우리말로는 회문이라고 부름

_ex) A man, a plan, a canal : Panama_

### [Answer 1] 리스트로 변환하여 활용하기

+ isalnum() : 영문자, 숫자 여부를 판별하는 함수

```python
strs = [] 
for char in s:
    if char.isalnums():
          strs.append(char.lower())
```
+ pop() : 리스트에서 원소를 뽑아와 삭제하는 함수, 인덱스 지정 가능

```python
while(len(strs)) > 1:
    if strs.pop(0) != strs.pop():
          return False
```
_pop()의 시간복잡도는 O(1)이지만,  pop(0)의 시간복잡도는 O(n)이므로 리스트를 큐처럼 이용하는 것은 바람직하지 않다._

### [Answer 2] 데크 자료형을 이용한 최적화

+ __데크 (Deque)__ : double-ended queue의 줄임말로 큐의 front와 rear에서 모두 삽입과 삭제가 가능한 큐

```python
# 자료형을 데크로 선언하기
strs = collection.deque()

# 리스트에서 이용한 pop(0) 부분 수정하기
while strs(len) > 1:
    if strs.popleft() != strs.pop():
        retrun False
```

### [Answer 3] 슬라이싱 사용

+ isalnum()으로 일일이 문자를 확인하지 않고 한 번에 영숫자(Alphanumeric)만 걸러내도록 정규식 처리
+ [정규식 관련 정리](https://github.com/ryuruz/Algorithm/blob/main/Python%20Grammer/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D.md)

```python
strs = strs.lower()
strs = re.sub('[^a-z0-9]', '', s)
```

### [Answer 4] C 구현
+ 문자열을 저장하는 char 포인터를 이용함
+ 속도 가장 빠름
