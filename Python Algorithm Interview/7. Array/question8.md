# LeetCode 42. Trapping Rain Water
높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.  

EX) [2,0,2,0,1]를 입력받은 경우 아래와 같은 모양으로, 물이 총 3만큼 들어갈 수 있다.

| 비 |

| 비 | 비 |


### [Answer 1] 투 포인터를 최대로 이동

+ 양 끝쪽에 left & right 포인터를 두고, 최대 기둥의 높이에 도달하도록 각 포인터를 가운데로 이동시킴
  + 최대 높이에 도달하는 기준 : left_max와 right_max를 비교해서, 더 값이 작은 쪽의 포인터를 이동시킴

+ volume : 양 쪽 기둥의 높이 차

#### 1. 초기화
```python
volume = 0
left, right = 0, len(height) -  1
left_max, right_max = height[left], height[right] # 초반에는 맨 처음 값을 max값으로 지정
```
#### 2. left < right 인 동안 가운데를 향하여 포인터가 이동하도록 함
```python
while left < right:
  left_max, right_max = max(height[left], left_max), max(height[right], right_max) #인덱스가 변경되었으므로 max값 업데이트
  
  if left_max <= right_max # left_max가 최대값과 더 차이가 많이 나는 상황이므로, left를 가운데로 이동시키기 위해서(⇢) 인덱스를 키워줘야 함 
    volume += left_max - height[left]
    left += 1
    
  else: # right_max가 최대값과 더 차이가 많이 나는 상황이므로, right를 가운데로 이동시키기 위해서(⇠) 인덱스를 줄여줘야 함
    volume += right_max - height[right]
    right -= 1
```
 
### [Answer 2] 스택 쌓기

+ __스택 (Stack)__ : 후입선출(LIFO) 방식을 따르는 자료구조

  + push() : 요소를 추가
  + pop() : 가장 최근에 삽입된 요소를 제거
___
+ 리스트의 요소들을 스택에 쌓아 나가면서, 기존의 높이보다 현재 입력된 높이가 더 높을 때 그 격차만큼 volume을 계산함
