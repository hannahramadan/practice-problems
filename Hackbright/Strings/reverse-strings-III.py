def reverseWords(s):
    """
    https://leetcode.com/problems/reverse-words-in-a-string-iii/

    Given a string s, reverse the order of characters in each word within a sentence 
    while still preserving whitespace and initial word order.

    >>> Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"

    >>> Input: s = "God Ding"
    Output: "doG gniD"

    """
    # Take out each word and add it to an empty list
    words_list = s.split(" ")
    
    # Go through each list item/word, replace the current word with a reversed version
    for i, item in enumerate(words_list):
        words_list[i] = item[::-1]
    
    #Join the list back together by spaces
    return " ".join(words_list)