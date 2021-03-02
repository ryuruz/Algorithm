import collections

def groupAnagrams(self, strs):
  anagrams = collections.defaultdict(list)
  
  for word in strs:
    anagrams[''.join(sorted(word))].append(word)
  return anagrams.values()
