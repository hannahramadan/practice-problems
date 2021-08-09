def reverse_words(arr):
'''You are given an array of characters arr that consists of sequences of 
characters separated by space characters. Each space-delimited sequence of characters 
defines a word.

input:  arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

output: [ 'p', 'r', 'a', 'c', 't', 'i', 'c', 'e', '  ',
          'm', 'a', 'k', 'e', 's', '  ',
          'p', 'e', 'r', 'f', 'e', 'c', 't' ]
'''  

  arr.reverse()  
  tracker = 0
  
  for i in range(len(arr)):
    if arr[i] == " ":
      arr[tracker:i] = reversed(arr[tracker:i])
      tracker = i+1
    elif i == len(arr)-1:
        arr[tracker:i+1] = reversed(arr[tracker:i+1])
      
  return arr