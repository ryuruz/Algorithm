# LeetCode 5. Longest Palindrome Substring
가장 긴 팰린드롬 부분 문자열을 출력하라

### [Answer 1] 중앙을 중심으로 확장하는 풀이

투 포인터를 이용하여, 중앙을 중심으로 확장하는 형태의 풀이

ex) babad

글자수가 홀수인 팰린드롬을 판별하기 위해 세 칸의 포인터 이동 ☐☐☐ → : bab, aba, bad

글자수가 짝수인 팰린드롬을 판별하기 위해 두 칸의 포인터 이동 ☐☐ → : ba, ab, ba, ad

+ 먼저 예외 처리를 진행한다.

```python
if len(s) < 2 or s == s[::-1]:
  return s
```

+ expand() 함수를 정의하여, 두 포인터가 팰린드롬 여부를 판별하면서 우측으로 이동하도록 구현

```python
def expand(left: int, right: int): 
  while left >= 0 and right <= len(s) and s[left] == s[right - 1]:
    left -= 1
    right -= 1
  return s[left+1:right-1]
```
```python  
for i in range(0, len(s)-1):
  result = max(result, expand(s, i, i+1), expand(s, i, i+2), key = len)
return result
```
