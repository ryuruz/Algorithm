# LeetCode 937. Reorder Log Files
로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.


### [Answer 1] 람다와 + 연산자 이용

문자로 구성된 로그가 숫자 로그보다 앞에 와야 하므로, 문자와 숫자를 구분해야 한다.

```python
if log.split()[1].isdigit():
  digits.append(log)
else:
  letters.append(log)
```
