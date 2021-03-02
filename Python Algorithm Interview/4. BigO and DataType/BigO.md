# 빅오(big-O) 표현법
+ 입력값이 무한대로 향할 때 함수의 상한을 설명하는 수학적 표기 방법
+ 점근적 실행 시간(Asymptotic Running time)을 표기할 때 가장 널리 쓰임, 달리 말하면 시간 복잡도라고 할 수 있음
  + 시간 복잡도(Time Complexity) : 어떤 알고리즘을 수행하는 데 걸리는 시간을 설명하는 계산 복잡도(Computational Complexity)
  + 계산 복잡도를 표기하는 가장 대표적인 방법 -> 빅오표현법
___
+ 시간복잡도를 표현하는 방법
  + 최고차항만을 표기함
  ex) ![CodeCogsEqn](https://user-images.githubusercontent.com/77661701/109608110-b2b7b380-7b6c-11eb-922c-23db89b38d2e.gif)
↦ ![CodeCogsEqn](https://user-images.githubusercontent.com/77661701/109608161-ca8f3780-7b6c-11eb-9ef3-31157ce006bb.png)

  + 계수는 무시함 
  ex) ![CodeCogsEqn (1)](https://user-images.githubusercontent.com/77661701/109608470-47221600-7b6d-11eb-8f88-565598b8b890.png)
↦ ![CodeCogsEqn](https://user-images.githubusercontent.com/77661701/109608161-ca8f3780-7b6c-11eb-9ef3-31157ce006bb.png)

+ 빅오 표현법의 종류

![bIG-0](https://user-images.githubusercontent.com/77661701/109611955-61aabe00-7b72-11eb-99cb-d8770edefe90.png)

  + ![CodeCogsEqn (3)](https://user-images.githubusercontent.com/77661701/109608885-ea732b00-7b6d-11eb-87ad-faecfd33be90.png)
    1. 입력값이 아무리 커도 실행시간이 일정
    2. 최고의 알고리즘이라고 할 수 있음
    
    _ex) 해시 테이블의 조회 및 삽입_
    
  + ![CodeCogsEqn (2)](https://user-images.githubusercontent.com/77661701/109608822-d4fe0100-7b6d-11eb-8b60-4853c50cb4f0.png)
    1. 매우 큰 입력값에도 크게 영향을 받지 않는 편으로, 웬만한 n에 있어서는 매우 견고함
    
    _ex) 이진검색_
    
  + ![CodeCogsEqn (4)](https://user-images.githubusercontent.com/77661701/109609356-8f8e0380-7b6e-11eb-8c76-35bedfa0fdfa.png)
    1. 입력값만큼 실행 시간에 영향을 받는, 알고리즘을 수행하는 데 걸리는 시간이 입력값에 비례하는 경우
    2. 선형 시간 알고리즘
    
    _ex) 정렬되지 않은 리스트에서 원소 꺼내기(최댓값,최솟값 등)_
    
  + ![CodeCogsEqn (5)](https://user-images.githubusercontent.com/77661701/109610439-1c858c80-7b70-11eb-9b2c-f868bb3f54f1.png)
    1. 대부분의 효율 좋은 알고리즘이 이에 해당함
    2. 적어도 모든 수에 대해 한 번 이상 비교해야 하는 비교 기반의 정렬 알고리즘은 아무리 좋은 알고리즘이라도 이보다 빠를 수 없음
    
    _ex) 병합 정렬_
    
  + ![CodeCogsEqn (6)](https://user-images.githubusercontent.com/77661701/109611018-f4e2f400-7b70-11eb-839c-cab1c8c3ad5a.png)
    1. 비효율적인 정렬 알고리즘
    
    _ex) 버블 정렬_
  
  + ![CodeCogsEqn (7)](https://user-images.githubusercontent.com/77661701/109611100-13e18600-7b71-11eb-812b-ad2c7b4a6f33.png)
    1. n이 작은 경우에는 ![CodeCogsEqn](https://user-images.githubusercontent.com/77661701/109611191-34a9db80-7b71-11eb-9820-9608c86513b9.png)과 비슷하지만, n이 커질수록 ![CodeCogsEqn (8)](https://user-images.githubusercontent.com/77661701/109611248-48edd880-7b71-11eb-89c4-831c49267f68.png)이 더 큼
   
   _ex) 피보나치 수를 재귀로 계산하는 알고리즘_
    
  + ![CodeCogsEqn (9)](https://user-images.githubusercontent.com/77661701/109611322-69b62e00-7b71-11eb-9766-88dc268ed5e2.png)
    1. 가장 느린 알고리즘
    2. 입력값이 조금만 커져도 웬만한 다항 시간 내에서 계산이 어려움

  + ![CodeCogsEqn](https://user-images.githubusercontent.com/77661701/109611191-34a9db80-7b71-11eb-9820-9608c86513b9.png)과 ![CodeCogsEqn (8)](https://user-images.githubusercontent.com/77661701/109611248-48edd880-7b71-11eb-89c4-831c49267f68.png)을 비교하는 코드
  ```python
  for n in range(1,15+1):
    print(n, n**2, 2**n)
  ```
  
+ 상한과 최악
  + 빅오 표기법은 상한(Upper Bound)를 의미함
  + 빅오메가 : 하한(Lower Bound) 의미
  + 빅세타 : 평균 의미
    + 복잡한 함수 f(x)가 있을 때, 이 함수가 가장 빨리 실행되는 경우가 하한,  가장 늦게 실행될 때가 상한
    
+ 분할 상환 분석 (Amortized Analysis) : 알고리즘의 복잡도를 계산할 때, 알고리즘 전체를 보지 않고 최악의 경우만을 보는 것은 지나치게 비관적이라는 이유로 등장한 방법

+ 병렬화 : 일부 알고리즘의 실행 속도를 높일 수 있는 방법
  + GPU : 대표적인 병렬 연산을 위한 장치

