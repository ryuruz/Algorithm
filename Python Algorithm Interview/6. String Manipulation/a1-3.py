import re 

def isPalindrome(s):
  s = s.lower()  
  s = re.sub('[^z-a0-9]', '', s)
  
  return s == s[::-1]
