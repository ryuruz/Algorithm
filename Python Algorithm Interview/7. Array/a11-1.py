for productExceptSelf(self, nums):
  out = []
  p = 1
  
  for i in range(0, len(nums)):
    out.append(p)
    p = p * nums[i]
    
  p = 1
  for i in range(len(nums) - 1, -1, -1):
    out[i] = out[i] * p
    p = nums[i] * p
    
  return out
