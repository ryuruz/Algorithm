def trap(self, height):
  
  # 리스트와 변수 초기화
  stack = []
  volume = 0
  
  for i in range(len(height)):
    
    while stack and height[i] > height[stack[-1]]: # i가 1 이상인 경우부터 실행 / 스택에 먼저 들어가있는 값(height[stack[-1]])보다 들어갈 값(height[i])이 더 클 때 
      top = stack.pop() 
      
      if not len(stack): # 스택이 비었는지 확인
        break # while문 빠져 나감
      
      # 어려움
      distacne = i - stack[-1] - 1
      waters = min(height[i], height[stack[-1]]) - height[top]
      
      volume += distacne * waters
      
   stack.append(i) # 스택에 직접 높이 값을 삽입하는 것이 아니라 인덱스를 넣는다는 점에 유의 !! 
  
 return volume
