# LeetCode 937. Reorder Log Files
로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.


### [Answer 1] 람다와 + 연산자 이용

문자로 구성된 로그가 숫자 로그보다 앞에 와야 하므로, 문자와 숫자를 구분해야 한다.
```python
# 숫자 로그는 digits에, 문자 로그는 letters에 추가
if log.split()[1].isdigit(): # 각 로그에서 식별자[0] 다음인 원소[1]를 기준으로 판별
  digits.append(log)
else:
  letters.append(log)
```
문자 로그가 letters에 모두 추가되면, 정렬한다.
```python
# 식별자를 제외한 문자열 [1:]을 키로 하여 정렬하고, 동일한 경우 식별자 [0]를 지정하여 정렬되도록 람다표현식을 이용 
letters.sort(key = lambda x: (x.split()[1:], x.split()[0]))
```
