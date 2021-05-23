# LeetCode 242. Valid Anagram
t가 s의 애너그램인지 판별하라
+ 애너그램 : 단어나 문장을 구성하고 있는 문자의 순서를 바꾸어 다른 단어나 문장을 만드는 것
+ 
### [Answer 1] 정렬을 이용한 비교 
+ 양쪽 문자열을 모두 정렬하여 그 상태가 일치하는지 확인하면 된다.

```python
def isAnagram(s, t):
  return sorted(s) == sorted(t)
```
