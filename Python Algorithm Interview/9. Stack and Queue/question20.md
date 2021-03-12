# LeetCode 20. Vaild-Parentheses

괄호로 된 입력값이 올바른지 판별하라

EX) () [] {}

output: True

### [Answer 1] 스택 일치 여부 판별

+ ( [ { 가 들어오면 스택에 push하고, } ] )를 만날 때 스택에서 pop한 결과가 매핑 테이블 결과와 매칭되는지 확인
    + 매핑 테이블을 만들어 놓고, 테이블에 존재하지 않으면 push
    + 결과가 일치하지 않으면 False 리턴

```python
stack = []
table = {
    ')' : '(',
    '}' : '{',
    '[' : ']'
}

if char not in table:
    stack.append(char)
elif table[char] != stack.pop():
    return False
```

+ 예외 처리

```python
return len(stack) == 0
```