# LeetCode 49. Group Anagrams
문자열 배열을 받아 애너그램 단위로 그룹핑하라.

## 애너그램 (Anagram)
- 일종의 언어유희로, 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말함


### [Answer 1] 정렬하여 딕셔너리에 추가

애너그램을 판단하는 가장 간단한 방법은 정렬하여 비교하는 것이다.

+ sorted() : 문자열을 정렬한 후,  리스트 형태로 리턴하는 함수
+ join() : 리스트의 문자열을 합치는 함수

애너그램끼리는 같은 키를 갖게된다.

```python
anagrams[''.join(sorted(word))].append(word)
```


정렬한 값을 키로 하여 딕셔너리에 추가하려고 한다.

존재하지 않는 키를 삽입하려고 하면 KeyError가 발생하므로, defaultdict()을 사용한다.

```python
anagrams = collections.defaultdict(list)
```
