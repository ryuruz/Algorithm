def trap(self, height):
  
  if not height: # height이 빈 리스트인지 확인
    return 0
  
  volume = 0
  left, right = 0, len(height) - 1
  left_max, right_max = height[left], height[right]
  
  while left < right:
    left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
    
    if left_max < right_max:
      volume += left_max - height[left]
      right += 1
    else:
      volume += right_max - height[right]
      right -= 1
      
  return volume
