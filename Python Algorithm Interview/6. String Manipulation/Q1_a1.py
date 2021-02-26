def isPalindrome(s:str):
  strs = []
  for char in s:
    if char.isalnum():
      str.append(char.lower())
    
  while len(strs) > 1:
    if strs.pop(0) != strs.pop():
      return False
    
  return True
