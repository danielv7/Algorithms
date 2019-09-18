#This question I first saw on LeetCode.

#Given a non-empty string containing only digits, determine the total number of ways to decode it.
#'A' -> 1
#'B' -> 2
#...
#'Z' -> 26
#Example: Input "226"
#Output 3: 
#Explanation: "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

#Time: O(n) Space: O(1)
def numWaysDecoding(string):
  if not string or string[0] == '0':
    return 0
  n = len(string)
  count1 = 1
  count2 = 1
  for i in range(1, n):
    if string[i] == '0':
      if string[i - 1] not in '12':
        return 0 
      else:
        count = count1
    else:
      if 10 <= int(string[i - 1:i + 1]) <= 26:
        count = count1 + count2
      else:
        count = count2
    count1, count2 = count2, count
  return count2
     
