# Is the word an anagram of a palindrome?
# A palindrome is a word that reads the same forward and backwards (eg, “racecar”, “tacocat”). 
# An anagram is a rescrambling of a word (eg for “racecar”, you could rescramble this as “arceace”).
# Determine if the given word is a re-scrambling of a palindrome.
# The word will only contain lowercase letters, a-z.


def is_anagram_of_palindrome(word):
  
  wordl = word.lower()
    
  word_count = {}
  odd_count = 0
  
  for char in wordl:
    word_count[char] = word_count.get(char, 0) + 1
    
  for item in word_count:
    if word_count[item] % 2 == 0:
      continue
    else:
      odd_count = odd_count + 1
      if odd_count > 1:
        return False
    
  return True 