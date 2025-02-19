"""
Student information for this assignment:

Replace <FULL NAME> with your name.
On my/our honor, Jason Li and Skyler Nguyen, this 
programming assignment is my own work and I have not provided this code to 
any other student.

I have read and understand the course syllabus's guidelines regarding Academic
Integrity. I understand that if I violate the Academic Integrity policy (e.g.
copy code from someone else, have the code generated by an LLM, or give my
code to someone else), the case shall be submitted to the Office of the Dean of
Students. Academic penalties up to and including an F in the course are likely.

UT EID 1: jxl237
UT EID 2: sn28523
"""


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n3(s):
    """
    Finds the length of the longest substring without repeating characters
    using a brute force approach (O(N^3)).

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    n = len(s)
    longest = 0
    for i in range(n):
      for j in range(i+1,n+1):
            substring = s[i:j]
            if len(substring) == len(set(substring)):
                  longest = max(longest, j - i)       
    return longest


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n2(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N^2)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    n = len(s)
    longest = 0
    for i in range(n):
        freq_map = {}
        for j in range(i,n):
            char = s[j]
            if char in freq_map:
                break
            freq_map[char] = True
            longest = max(longest, j - i + 1)
    return longest


# TODO: implement this function. You may delete this comment when you are done.
def length_of_longest_substring_n(s):
    """
    Finds the length of the longest substring without repeating characters
    using a frequency list approach (O(N)), converting each character to
    their corresponding numeric representation in ASCII as the index into the
    frequency list. However, this approach stops early, breaking out of the inner
    loop when a repeating character is found. You may also choose to challenge
    yourself by implementing a sliding window approach.

    pre: s is a string of arbitrary length, possibly empty.
    post: Returns an integer >= 0 representing the length of the longest substring
          in s that contains no repeating characters.
    """
    n = len(s)
    if n == 0:
        return 0
    longest = 0
    left = 0
    last_index = {}
    for right, char in enumerate(s):
        if char in last_index and last_index[char] >= left:
            left = last_index[char] + 1
        last_index[char] = right
        current_length = right - left + 1
        if current_length > longest:
            longest = current_length
    return longest
