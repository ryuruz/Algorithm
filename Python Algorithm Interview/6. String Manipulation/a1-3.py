import re 

def isPalindrome(s):
  s = s.lower()  
  s = re.sub('[^a-z0-9]', '', s)
  
  return s == s[::-1] #원래 문자열과 뒤집은 문자열이 같은지 확인
